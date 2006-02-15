#ifndef FWCore_MessageService_MessageLoggerSpigot_h
#define FWCore_MessageService_MessageLoggerSpigot_h


#include "boost/thread/thread.hpp"


namespace edm  {
namespace service {       


class MessageLoggerSpigot
{
public:
  // ---  birth/death:
  MessageLoggerSpigot();
  ~MessageLoggerSpigot();

private:
  // --- no copying:
  MessageLoggerSpigot( MessageLoggerSpigot const & );
  void  operator = ( MessageLoggerSpigot const & );

  // --- data:
  boost::thread  scribe;

};  // MessageLoggerSpigot


}   // end of namespace service
}  // namespace edm


#endif  // FWCore_MessageService_MessageLoggerSpigot_h
