// Copyright 2009-2021 NTESS. Under the terms
// of Contract DE-NA0003525 with NTESS, the U.S.
// Government retains certain rights in this software.
//
// Copyright (c) 2009-2021, NTESS
// All rights reserved.
//
// Portions are copyright of other developers:
// See the file CONTRIBUTORS.TXT in the top level directory
// the distribution for more information.
//
// This file is part of the SST software package. For license
// information, see the LICENSE file in the top level directory of the
// distribution.


#ifndef _H_EMBER_TEST
#define _H_EMBER_TEST

#include "mpi/embermpigen.h"
#include "rng/xorshift.h"

namespace SST {
namespace Ember {

class EmberTestGenerator : public EmberMessagePassingGenerator {

public:
    SST_ELI_REGISTER_SUBCOMPONENT_DERIVED(
        EmberTestGenerator,
        "ember",
        "TestMotif",
        SST_ELI_ELEMENT_VERSION(1,0,0),
        "Performs a Test Motif",
        SST::Ember::EmberGenerator
    )

    // used as an empty motif test for background
    SST_ELI_DOCUMENT_PARAMS(
        {   "arg.iterations",       "Sets the number of ping pong operations to perform",   "1"},
        {   "arg.compute",          "Sets the wait mode",   "1"},
        {   "arg.wait2start",          "Sets the wait mode",   "1"},
    )

    SST_ELI_DOCUMENT_STATISTICS(
        { "time-Init", "Time spent in Init event",          "ns",  0},
        { "time-Finalize", "Time spent in Finalize event",  "ns", 0},
        { "time-Rank", "Time spent in Rank event",          "ns", 0},
        { "time-Size", "Time spent in Size event",          "ns", 0},
        { "time-Send", "Time spent in Recv event",          "ns", 0},
        { "time-Recv", "Time spent in Recv event",          "ns", 0},
        { "time-Irecv", "Time spent in Irecv event",        "ns", 0},
        { "time-Isend", "Time spent in Isend event",        "ns", 0},
        { "time-Wait", "Time spent in Wait event",          "ns", 0},
        { "time-Waitall", "Time spent in Waitall event",    "ns", 0},
        { "time-Waitany", "Time spent in Waitany event",    "ns", 0},
        { "time-Test", "Time spent in Test event",    "ns", 0},
        { "time-Compute", "Time spent in Compute event",    "ns", 0},
        { "time-Barrier", "Time spent in Barrier event",    "ns", 0},
        { "time-Alltoallv", "Time spent in Alltoallv event", "ns", 0},
        { "time-Alltoall", "Time spent in Alltoall event",  "ns", 0},
        { "time-Allreduce", "Time spent in Allreduce event", "ns", 0},
        { "time-Reduce", "Time spent in Reduce event",      "ns", 0},
        { "time-Bcast", "Time spent in Bcast event",        "ns", 0},
        { "time-Gettime", "Time spent in Gettime event",    "ns", 0},
        { "time-Commsplit", "Time spent in Commsplit event", "ns", 0},
        { "time-Commcreate", "Time spent in Commcreate event", "ns", 0},
    )

public:

	EmberTestGenerator(SST::ComponentId_t id, Params& params):
        EmberMessagePassingGenerator(id, params, "Null" ), m_phase(Init)
	{
		// m_rng = new SST::RNG::XORShiftRNG();

        //
        m_loopIndex = 0;
        m_iterations = (uint32_t) params.find("arg.iterations", 1);
	    m_compute    = (uint64_t) params.find("arg.compute", 0);
        m_wait2start = (uint64_t) params.find("arg.wait2start", 1);
        
        if(rank() == 0) {
            printf("-----------EmberTestMotif size: %d---------\n", size());
            printf("iterations: %u\n", m_iterations);
            printf("compute: %lu\n", m_compute);
            printf("wait2start: %lu\n", m_wait2start);
        }
	}

    bool generate( std::queue<EmberEvent*>& evQ){
		// assert( size() == 2 );
		// switch ( m_phase ) {
		// 	case Init:
		// 		m_rng->seed( rank() + getSeed() );
		// 		if ( rank() == 0 ) {
		// 		 	enQ_irecv( evQ, NULL, 0, CHAR, 1, 0xdeadbeef, GroupWorld, &m_req );
		// 			enQ_test( evQ, &m_req, &m_flag, &m_resp );
		// 			m_phase = Check;
		// 			return false;
		// 		} else {
		// 			enQ_compute( evQ, m_rng->generateNextUInt32() % 1000000 );
		// 			enQ_send( evQ, NULL, 0, CHAR, 0, 0xdeadbeef, GroupWorld );
		// 			return true;
		// 		}

		// 	case Check:

		// 		if ( m_flag ) {
		// 			printf("src=%d\n", m_resp.src );
		// 			return true;
		// 		} else {
		// 			enQ_compute( evQ, 10000 );
		// 			printf("test again\n" );
		// 			enQ_test( evQ, &m_req, &m_flag, &m_resp );
		// 			return false;
		// 		}
		// }
		// assert(0);

        //

        if(m_loopIndex == m_iterations){
            if(rank() == 0){
                printf("EmberTestMotif finish, start@ %lu, end@ %lu, lat: %lu\n", m_startTime, m_stopTime, m_stopTime-m_startTime);
            }
            return true;
        }

        if(m_loopIndex == 0){
            enQ_compute( evQ, m_wait2start );
            enQ_getTime( evQ, &m_startTime );
        } 

        enQ_compute( evQ, m_compute);
        enQ_getTime( evQ, &m_stopTime );

        m_loopIndex++;
        return false;
	}

private:

	unsigned int getSeed() {
        struct timeval start;
        gettimeofday( &start, NULL );
        return start.tv_usec;
    }

	SST::RNG::XORShiftRNG* m_rng;
	int m_flag;
	enum { Init, Check } m_phase;
	MessageRequest  m_req;
    MessageResponse m_resp;


    //
    uint32_t m_loopIndex;
    uint64_t m_compute;
	uint32_t m_iterations;
    uint64_t m_wait2start;

    uint64_t  m_startTime;
    uint64_t  m_stopTime;
};

}
}

#endif
