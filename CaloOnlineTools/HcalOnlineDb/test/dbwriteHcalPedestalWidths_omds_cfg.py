import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.MessageLogger=cms.Service("MessageLogger",
                              destinations=cms.untracked.vstring("cout"),
                              cout=cms.untracked.PSet(
                              treshold=cms.untracked.string("INFO")
                              )
)

process.load("CondCore.CondDB.CondDB_cfi")
process.CondDB.connect = cms.string('sqlite_file:testExample.db')
process.CondDB.DBParameters.authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb')

process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    firstValue = cms.uint64(1),
    lastValue = cms.uint64(1),
    interval = cms.uint64(1)
)

process.es_ascii = cms.ESSource("HcalOmdsCalibrations",
    input = cms.VPSet(cms.PSet(
        object = cms.string('PedestalWidths'),
        tag = cms.string('hcal-pedwidth-test-v1'),
        version = cms.string('hcal-pedwidth-test-v1'),
        subversion = cms.int32(1),
        accessor = cms.string('occi://CMS_HCL_APPUSER_R@anyhost/cms_omds_lb?PASSWORD=HCAL_Reader_44,LHWM_VERSION=22'),
        query = cms.string('''
SELECT 
      OBJECTNAME, 
      SUBDET, 
      IETA, 
      IPHI, 
      DEPTH, 
      TYPE, 
      SECTION, 
      ISPOSITIVEETA, 
      SECTOR, 
      MODULE, 
      CHANNEL, 
      IS_ADC_COUNTS, 
      COVARIANCE_00, 
      COVARIANCE_01, 
      COVARIANCE_02, 
      COVARIANCE_03, 
      COVARIANCE_10, 
      COVARIANCE_11, 
      COVARIANCE_12, 
      COVARIANCE_13, 
      COVARIANCE_20, 
      COVARIANCE_21, 
      COVARIANCE_22, 
      COVARIANCE_23, 
      COVARIANCE_30, 
      COVARIANCE_31, 
      COVARIANCE_32, 
      COVARIANCE_33 
FROM ( 
     select 
            MIN(theview.record_id) as record_id, 
            MAX(theview.interval_of_validity_begin) as iov_begin, 
            theview.channel_map_id 
     from 
            cms_hcl_hcal_cond.V_HCAL_PEDESTAL_WIDTHS_V3 theview 
     where 
            tag_name=:1 
     AND 
            theview.interval_of_validity_begin<=:2 
     group by 
            theview.channel_map_id 
     order by 
            theview.channel_map_id 
) fp 
inner join CMS_HCL_HCAL_COND.V_HCAL_PEDESTAL_WIDTHS_V3 sp 
on 
fp.record_id=sp.record_id 
        ''')
    ))
)

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    process.CondDB,
    timetype = cms.untracked.string('runnumber'),
    logconnect= cms.untracked.string('sqlite_file:log.db'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('HcalPedestalWidthsRcd'),
        tag = cms.string('hcal_resp_corrs_trivial_mc')
         ))
)

process.mytest = cms.EDAnalyzer("HcalPedestalWidthsPopConAnalyzer",
    record = cms.string('HcalPedestalWidthsRcd'),
    loggingOn= cms.untracked.bool(True),
    SinceAppendMode=cms.bool(True),
    Source=cms.PSet(
#    firstSince=cms.untracked.double(300) 
    IOVRun=cms.untracked.uint32(1)
    )
)

process.p = cms.Path(process.mytest)
