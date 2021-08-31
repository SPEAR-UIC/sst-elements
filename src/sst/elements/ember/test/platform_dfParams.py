
debug = 0

#72 node df
# netConfig = {
#     "topology": "dragonfly", # not read here. topo is provided as emberLoad para
#     "shape": "2:4:1:9",
#     'num_groups': 9,
#     'routers_per_group': 4, 
#     'hosts_per_router': 2,
#     'intergroup_links': 1,
#     #'algorithm': "minimal", # par ugal-4vc q-routing1 minimal valiant
# }

# DF topo params 342 nodes 
netConfig = {
    "topology": "dragonfly", # not read here. topo is provided as emberLoad para
    "shape": "3:6:1:19",
    'num_groups': 19,
    'routers_per_group': 6, 
    'hosts_per_router': 3,
    'intergroup_links': 1,
    #'algorithm': "ugal-4vc", # par ugal-4vc q-routing1
}

# DF 1056 nodes 
# netConfig = {
#     "topology": "dragonfly", # not read here. topo is provided as emberLoad para
#     "shape": "4:8:1:33",
#     'num_groups': 33,
#     'routers_per_group': 8, 
#     'hosts_per_router': 4,
#     'intergroup_links': 1,
#     # 'algorithm': "ugal-4vc", # par ugal-4vc q-routing1
# }

rtingParams_q = {
    "learning_rate": 0.2,
    "learning_rate2": 0.04,
    "epsilon": 0.001,
    "q_threshold1": 0.2,
    "q_threshold2": 0.35,
    "max_hops": 1,
    
    "qtable_row_type": "destG_srcN",
    "src_group_q": False,
    "src_mid_group_q": True,

    "qtable_bcast": "nobcast",
    # "qbcastThsld": ,
    # "qbcastPerid": ,

    "save_qtable": False,
    # "save_qtable_time": ,
    "load_qtable": False,
    # "pathToQtableFile": ,
    "perid_func": False ,
}

rtingParams_adp = {
    "adaptive_threshold": 2.0
}

networkParams = {
    "packetSize" : "128B",
    "flitSize" : "128B",
    "link_bw" : "4GB/s",
    "xbar_bw" : "40GB/s",
    # "link_lat" : "40ns",
    "link_lat_host" : "10ns",
    "link_lat_local" : "30ns",
    "link_lat_global" : "300ns",
    "input_latency" : "10ns",
    "output_latency" : "10ns",
    "input_buf_size" : "2560B",
    "output_buf_size" : "2560B",

    #yao
    "xbar_arb" : "merlin.xbar_arb_lru",

}

nicParams = {
    # "numVNs" : 1,
# !!!! yao
    "numVNs" : 1,

	"detailedCompute.name" : "thornhill.SingleThread",
    # "module" : "merlin.linkcontrol",
    "module" : "merlin.reorderlinkcontrol", ## for adp routing 
    "packetSize" : networkParams['packetSize'],
    "link_bw" : networkParams['link_bw'],
    "input_buf_size" : networkParams['input_buf_size'],
    "output_buf_size" : networkParams['output_buf_size'],
    "rxMatchDelay_ns" : 10, # 100,  #!!!!
    "txDelay_ns" : 5, #50, !!!!
    "nic2host_lat" : "5ns",  ### "150ns", #"10ns", # "150ns",   !!!!!!
    "useSimpleMemoryModel" : 0,
# simpleMemoryModel.verboseMask: values 
#define BUS_WIDGET_MASK 1<<1
#define CACHE_MASK      1<<2
#define LOAD_MASK       1<<3
#define MEM_MASK        1<<4
#define MUX_MASK        1<<5
#define STORE_MASK      1<<6
#define THREAD_MASK     1<<7
#define BUS_BRIDGE_MASK 1<<8
	# "simpleMemoryModel.verboseLevel" : 0,
	# "simpleMemoryModel.verboseMask" : -1,

    "simpleMemoryModel.verboseLevel" : 100,
	"simpleMemoryModel.verboseMask" : 1,

	"simpleMemoryModel.memNumSlots" : 32,
	"simpleMemoryModel.memReadLat_ns" : 15, #  !!!
	"simpleMemoryModel.memWriteLat_ns" : 4, #  !!!

	"simpleMemoryModel.hostCacheUnitSize" : 32, 
	"simpleMemoryModel.hostCacheNumMSHR" : 32, 
	"simpleMemoryModel.hostCacheLineSize" : 64, 

	"simpleMemoryModel.widgetSlots" : 32, 

	"simpleMemoryModel.nicNumLoadSlots" : 16, 
	"simpleMemoryModel.nicNumStoreSlots" : 16, 

	"simpleMemoryModel.nicHostLoadSlots" : 1, 
	"simpleMemoryModel.nicHostStoreSlots" : 1, 

	"simpleMemoryModel.busBandwidth_Gbs" : 7.8,
	"simpleMemoryModel.busNumLinks" : 8,
	"simpleMemoryModel.detailedModel.name" : "firefly.detailedInterface",
	"maxRecvMachineQsize" : 100,
	"maxSendMachineQsize" : 100,

    #"numVNs" : 7,

    #"getHdrVN" : 1,
    #"getRespSmallVN" : 2,
    #"getRespLargeVN" : 3,
    #"getRespSize" : 15000,

    #"shmemAckVN": 1 ,
    #"shmemGetReqVN": 2,
    #"shmemGetLargeVN": 3,
    #"shmemGetSmallVN": 4,
    #"shmemGetThresholdLength": 8,
    #"shmemPutLargeVN": 5,
    #"shmemPutSmallVN": 6,
    #"shmemPutThresholdLength": 8,

}

emberParams = {
    "os.module"    : "firefly.hades",
    "os.name"      : "hermesParams",
    "api.0.module" : "firefly.hadesMP",
    "api.1.module" : "firefly.hadesSHMEM",
    "api.2.module" : "firefly.hadesMisc",
    'firefly.hadesSHMEM.verboseLevel' : 0,
    'firefly.hadesSHMEM.verboseMask'  : -1,
    'firefly.hadesSHMEM.enterLat_ns'  : 7,
    'firefly.hadesSHMEM.returnLat_ns' : 7,
    'verbose' : 0, # yao !!!
    #yao
    'verboseMask': 1,   ## 0 print; 1 dont print
    # 'motifLog': 'motif.log',
    'firefly.hadesMP.verboseLevel' : 100,
    'firefly.hadesMP.verboseMask'  : 1,
}

hermesParams = {
	"hermesParams.detailedCompute.name" : "thornhill.SingleThread",
	"hermesParams.memoryHeapLink.name" : "thornhill.MemoryHeapLink",
    "hermesParams.nicModule" : "firefly.VirtNic",

    "hermesParams.functionSM.defaultEnterLatency" : 30000,
    "hermesParams.functionSM.defaultReturnLatency" : 30000,

##!!! yao

    # "hermesParams.functionSM.smallCollectiveVN" : 1,
    # "hermesParams.functionSM.smallCollectiveSize" : 0,
#!!!! yao
    #"hermesParams.ctrlMsg.rendezvousVN" : 1,
    # "hermesParams.ctrlMsg.ackVN" : 2,

#!!!! yao
    "hermesParams.ctrlMsg.shortMsgLength" : 12000,


    "hermesParams.ctrlMsg.matchDelay_ns" : 15,   #### !!!!!

    "hermesParams.ctrlMsg.txSetupMod" : "firefly.LatencyMod",
    "hermesParams.ctrlMsg.txSetupModParams.range.0" : "0-:13ns", #### !!!!!

    "hermesParams.ctrlMsg.rxSetupMod" : "firefly.LatencyMod",
    "hermesParams.ctrlMsg.rxSetupModParams.range.0" : "0-:10ns",#### !!!!!

    "hermesParams.ctrlMsg.txMemcpyMod" : "firefly.LatencyMod",
    "hermesParams.ctrlMsg.txMemcpyModParams.op" : "Mult",
    "hermesParams.ctrlMsg.txMemcpyModParams.range.0" : "0-:344ps",

    "hermesParams.ctrlMsg.rxMemcpyMod" : "firefly.LatencyMod",
    "hermesParams.ctrlMsg.txMemcpyModParams.op" : "Mult",
    "hermesParams.ctrlMsg.rxMemcpyModParams.range.0" : "0-:344ps",

    "hermesParams.ctrlMsg.sendAckDelay_ns" : 0,
    "hermesParams.ctrlMsg.regRegionBaseDelay_ns" : 300, # !!!affect rendezvous isend return time
    "hermesParams.ctrlMsg.regRegionPerPageDelay_ns" : 10, ## !!!
    "hermesParams.ctrlMsg.regRegionXoverLength" : 4096,
    "hermesParams.loadMap.0.start" : 0,
    "hermesParams.loadMap.0.len" : 2,
}
