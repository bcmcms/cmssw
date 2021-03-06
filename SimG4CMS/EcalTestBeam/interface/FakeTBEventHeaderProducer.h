#ifndef FakeTBEventHeaderProducer_H
#define FakeTBEventHeaderProducer_H
/*
 * \file FakeTBEventHeaderProducer.h
 *
 *
 * Mimic the event header information
 * for the test beam simulation 
 *
 */


#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "SimDataFormats/EcalTestBeam/interface/PEcalTBInfo.h"
#include "TBDataFormats/EcalTBObjects/interface/EcalTBEventHeader.h"
#include "Geometry/EcalTestBeam/interface/EcalTBHodoscopeGeometry.h"

class FakeTBEventHeaderProducer: public edm::stream::EDProducer <>
{  
public:
  
  /// Constructor
  explicit FakeTBEventHeaderProducer(const edm::ParameterSet& ps);
  
  /// Destructor
  virtual ~FakeTBEventHeaderProducer();
  
  /// Produce digis out of raw data
  void produce(edm::Event & event, const edm::EventSetup& eventSetup) override;
  
private:

  edm::EDGetTokenT<PEcalTBInfo> ecalTBInfo_;

};

#endif
