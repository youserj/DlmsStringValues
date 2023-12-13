from dataclasses import dataclass
from ...types import common_data_types as cdt
from ...cosem_interface_classes import overview


class ClassId(cdt.LongUnsigned):
    """ Class ID type """
    DEFAULT = 1

    def validate(self):
        if not int(self) in overview.ClassID.get_all_id():
            raise ValueError(F'Unknown DLMS class with ID {int(self)}')


@dataclass(frozen=True)
class ClassIDCDT:
    DATA = ClassId(int(overview.ClassID.DATA))
    REGISTER = ClassId(int(overview.ClassID.REGISTER))
    EXT_REGISTER = ClassId(int(overview.ClassID.EXT_REGISTER))
    DEMAND_REGISTER = ClassId(int(overview.ClassID.DEMAND_REGISTER))
    REGISTER_ACTIVATION = ClassId(int(overview.ClassID.REGISTER_ACTIVATION))
    PROFILE_GENERIC = ClassId(int(overview.ClassID.PROFILE_GENERIC))
    CLOCK = ClassId(int(overview.ClassID.CLOCK))
    SCRIPT_TABLE = ClassId(int(overview.ClassID.SCRIPT_TABLE))
    SCHEDULE = ClassId(int(overview.ClassID.SCHEDULE))
    SPECIAL_DAYS_TABLE = ClassId(int(overview.ClassID.SPECIAL_DAYS_TABLE))
    ASSOCIATION_SN_CLASS = ClassId(int(overview.ClassID.ASSOCIATION_SN))
    ASSOCIATION_LN_CLASS = ClassId(int(overview.ClassID.ASSOCIATION_LN))
    SAP_ASSIGNMENT = ClassId(int(overview.ClassID.SAP_ASSIGNMENT))
    IMAGE_TRANSFER = ClassId(int(overview.ClassID.IMAGE_TRANSFER))
    IEC_LOCAL_PORT_SETUP = ClassId(int(overview.ClassID.IEC_LOCAL_PORT_SETUP))
    ACTIVITY_CALENDAR = ClassId(int(overview.ClassID.ACTIVITY_CALENDAR))
    REGISTER_MONITOR = ClassId(int(overview.ClassID.REGISTER_MONITOR))
    SINGLE_ACTION_SCHEDULE = ClassId(int(overview.ClassID.SINGLE_ACTION_SCHEDULE))
    IEC_HDLC_SETUP = ClassId(int(overview.ClassID.IEC_HDLC_SETUP))
    IEC_TWISTED_PAIR__1__SETUP = ClassId(int(overview.ClassID.IEC_TWISTED_PAIR_1_SETUP))
    M_BUS_SLAVE_PORT_SETUP = ClassId(int(overview.ClassID.M_BUS_SLAVE_PORT_SETUP))
    UTILITY_TABLES = ClassId(int(overview.ClassID.UTILITY_TABLES))
    MODEM_CONFIGURATION = ClassId(int(overview.ClassID.MODEM_CONFIGURATION))
    AUTO_ANSWER = ClassId(int(overview.ClassID.AUTO_ANSWER))
    AUTO_CONNECT = ClassId(int(overview.ClassID.AUTO_CONNECT))
    COSEM_DATA_PROTECTION = ClassId(int(overview.ClassID.COSEM_DATA_PROTECTION))
    PUSH_SETUP = ClassId(int(overview.ClassID.PUSH_SETUP))
    TCP_UDP_SETUP = ClassId(int(overview.ClassID.TCP_UDP_SETUP))
    IPV4_SETUP = ClassId(int(overview.ClassID.IPV4_SETUP))
    PRIME_NB_OFDM_PLC_MAC_ADDRESS_SETUP = ClassId(int(overview.ClassID.PRIME_NB_OFDM_PLC_MAC_ADDRESS_SETUP))
    PPP_SETUP = ClassId(int(overview.ClassID.PPP_SETUP))
    GPRS_MODEM_SETUP = ClassId(int(overview.ClassID.GPRS_MODEM_SETUP))
    SMTP_SETUP = ClassId(int(overview.ClassID.SMTP_SETUP))
    GSM_DIAGNOSTIC = ClassId(int(overview.ClassID.GSM_DIAGNOSTIC))
    IPV6_SETUP = ClassId(int(overview.ClassID.IPV6_SETUP))
    S_FSK_PHY_MAC_SET_UP = ClassId(int(overview.ClassID.S_FSK_PHY_MAC_SET_UP))
    S_FSK_ACTIVE_INITIATOR = ClassId(int(overview.ClassID.S_FSK_ACTIVE_INITIATOR))
    S_FSK_MAC_SYNCHRONIZATION_TIMEOUTS = ClassId(int(overview.ClassID.S_FSK_MAC_SYNCHRONIZATION_TIMEOUTS))
    S_FSK_MAC_COUNTERS = ClassId(int(overview.ClassID.S_FSK_MAC_COUNTERS))
    IEC_61334_4_32_LLC_SETUP = ClassId(int(overview.ClassID.IEC_61334_4_32_LLC_SETUP))
    S_FSK_REPORTING_SYSTEM_LIST = ClassId(int(overview.ClassID.S_FSK_REPORTING_SYSTEM_LIST))
    ISO_IEC_8802_2_LLC_TYPE_1_SETUP = ClassId(int(overview.ClassID.ISO_IEC_8802_2_LLC_TYPE_1_SETUP))
    ISO_IEC_8802_2_LLC_TYPE_2_SETUP = ClassId(int(overview.ClassID.ISO_IEC_8802_2_LLC_TYPE_2_SETUP))
    ISO_IEC_8802_2_LLC_TYPE_3_SETUP = ClassId(int(overview.ClassID.ISO_IEC_8802_2_LLC_TYPE_3_SETUP))
    REGISTER_TABLE = ClassId(int(overview.ClassID.REGISTER_TABLE))
    COMPACT_DATA = ClassId(int(overview.ClassID.COMPACT_DATA))
    STATUS_MAPPING = ClassId(int(overview.ClassID.STATUS_MAPPING))
    SECURITY_SETUP = ClassId(int(overview.ClassID.SECURITY_SETUP))
    PARAMETER_MONITOR = ClassId(int(overview.ClassID.PARAMETER_MONITOR))
    SENSOR_MANAGER_INTERFACE_CLASS = ClassId(int(overview.ClassID.SENSOR_MANAGER_INTERFACE_CLASS))
    ARBITRATOR = ClassId(int(overview.ClassID.ARBITRATOR))
    DISCONNECT_CONTROL = ClassId(int(overview.ClassID.DISCONNECT_CONTROL))
    LIMITER = ClassId(int(overview.ClassID.LIMITER))
    M_BUS_CLIENT = ClassId(int(overview.ClassID.M_BUS_CLIENT))
    WIRELESS_MODE_Q_CHANNEL = ClassId(int(overview.ClassID.WIRELESS_MODE_Q_CHANNEL))
    M_BUS_MASTER_PORT_SETUP = ClassId(int(overview.ClassID.M_BUS_MASTER_PORT_SETUP))
    DLMS_COSEM_SERVER_M_BUS_PORT_SETUP = ClassId(int(overview.ClassID.DLMS_COSEM_SERVER_M_BUS_PORT_SETUP))
    M_BUS_DIAGNOSTIC = ClassId(int(overview.ClassID.M_BUS_DIAGNOSTIC))
    _61334_4_32_LLC_SSCS_SETUP = ClassId(int(overview.ClassID._61334_4_32_LLC_SSCS_SETUP))
    PRIME_NB_OFDM_PLC_PHYSICAL_LAYER_COUNTERS = ClassId(int(overview.ClassID.PRIME_NB_OFDM_PLC_PHYSICAL_LAYER_COUNTERS))
    PRIME_NB_OFDM_PLC_MAC_SETUP = ClassId(int(overview.ClassID.PRIME_NB_OFDM_PLC_MAC_SETUP))
    PRIME_NB_OFDM_PLC_MAC_FUNCTIONAL_PARAMETERS = ClassId(int(overview.ClassID.PRIME_NB_OFDM_PLC_MAC_FUNCTIONAL_PARAMETERS))
    PRIME_NB_OFDM_PLC_MAC_COUNTERS = ClassId(int(overview.ClassID.PRIME_NB_OFDM_PLC_MAC_COUNTERS))
    PRIME_NB_OFDM_PLC_MAC_NETWORK_ADMINISTRATION_DATA = ClassId(int(overview.ClassID.PRIME_NB_OFDM_PLC_MAC_NETWORK_ADMINISTRATION_DATA))
    PRIME_NB_OFDM_PLC_APPLICATION_IDENTIFICATION = ClassId(int(overview.ClassID.PRIME_NB_OFDM_PLC_APPLICATION_IDENTIFICATION))
    G3_PLC_MAC_LAYER_COUNTERS = ClassId(int(overview.ClassID.G3_PLC_MAC_LAYER_COUNTERS))
    G3_PLC_MAC_SETUP = ClassId(int(overview.ClassID.G3_PLC_MAC_SETUP))
    G3_PLC_MAC_6LOWPAN_ADAPTATION_LAYER_SETUP = ClassId(int(overview.ClassID.G3_PLC_MAC_6LOWPAN_ADAPTATION_LAYER_SETUP))
    WI_SUN_SETUP = ClassId(int(overview.ClassID.WI_SUN_SETUP))
    WI_SUN_DIAGNOSTIC = ClassId(int(overview.ClassID.WI_SUN_DIAGNOSTIC))
    RPL_DIAGNOSTIC = ClassId(int(overview.ClassID.RPL_DIAGNOSTIC))
    MPL_DIAGNOSTIC = ClassId(int(overview.ClassID.MPL_DIAGNOSTIC))
    NTP_SETUP = ClassId(int(overview.ClassID.NTP_SETUP))
    ZIGBEE_SAS_STARTUP = ClassId(int(overview.ClassID.ZIGBEE_SAS_STARTUP))
    ZIGBEE_SAS_JOIN = ClassId(int(overview.ClassID.ZIGBEE_SAS_JOIN))
    ZIGBEE_SAS_APS_FRAGMENTATION = ClassId(int(overview.ClassID.ZIGBEE_SAS_APS_FRAGMENTATION))
    ZIGBEE_NETWORK_CONTROL = ClassId(int(overview.ClassID.ZIGBEE_NETWORK_CONTROL))
    ZIGBEE_TUNNEL_SETUP = ClassId(int(overview.ClassID.ZIGBEE_TUNNEL_SETUP))
    ACCOUNT = ClassId(int(overview.ClassID.ACCOUNT))
    CREDIT_INTERFACE_CLASS = ClassId(int(overview.ClassID.CREDIT_INTERFACE_CLASS))
    CHARGE = ClassId(int(overview.ClassID.CHARGE))
    TOKEN_GATEWAY = ClassId(int(overview.ClassID.TOKEN_GATEWAY))
    FUNCTION_CONTROL = ClassId(int(overview.ClassID.FUNCTION_CONTROL))
    ARRAY_MANAGER = ClassId(int(overview.ClassID.ARRAY_MANAGER))
    COMMUNICATION_PORT_PROTECTION = ClassId(int(overview.ClassID.COMMUNICATION_PORT_PROTECTION))
    SCHC_LPWAN_SETUP = ClassId(int(overview.ClassID.SCHC_LPWAN_SETUP))
    SCHC_LPWAN_DIAGNOSTIC = ClassId(int(overview.ClassID.SCHC_LPWAN_DIAGNOSTIC))
    LoRaWAN_SETUP = ClassId(int(overview.ClassID.LoRaWAN_SETUP))
    LoRaWAN_DIAGNOSTIC = ClassId(int(overview.ClassID.LoRaWAN_DIAGNOSTIC))
    ISO_IEC14908_IDENTIFICATION = ClassId(int(overview.ClassID.ISO_IEC14908_IDENTIFICATION))
    ISO_IEC14908_PROTOCOL_SETUP = ClassId(int(overview.ClassID.ISO_IEC14908_PROTOCOL_SETUP))
    ISO_IEC14908_PROTOCOL_STATUS = ClassId(int(overview.ClassID.ISO_IEC14908_PROTOCOL_STATUS))
    ISO_IEC14908_PROTOCOL_DIAGNOSTIC = ClassId(int(overview.ClassID.ISO_IEC14908_PROTOCOL_DIAGNOSTIC))
    HS_PLC_ISO_IEC_12139_1_MAC_SETUP = ClassId(int(overview.ClassID.HS_PLC_ISO_IEC_12139_1_MAC_SETUP))
    HS_PLC_ISO_IEC_12139_1_CPAS_SETUP = ClassId(int(overview.ClassID.HS_PLC_ISO_IEC_12139_1_CPAS_SETUP))
    HS_PLC_ISO_IEC_12139_1_IP_SSAS_SETUP = ClassId(int(overview.ClassID.HS_PLC_ISO_IEC_12139_1_IP_SSAS_SETUP))
    HS_PLC_ISO_IEC_12139_1_HDLC_SSAS_SETUP = ClassId(int(overview.ClassID.HS_PLC_ISO_IEC_12139_1_HDLC_SSAS_SETUP))
    LTE_MONITORING = ClassId(int(overview.ClassID.LTE_MONITORING))
    CLIENT_SETUP = ClassId(int(overview.ClassID.CLIENT_SETUP))

    @classmethod
    def get_all_id(cls) -> tuple[int]:
        """return all id container in build-in <int>"""
        return tuple(map(int, filter(lambda it: isinstance(it, ClassId), cls.__dict__.values())))


class ServerSAP(cdt.LongUnsigned):

    def validate(self):
        if int.from_bytes(self.contents, 'big') > 0x3FFF:
            raise ValueError(F'The range for the server_SAP is 0x000…0x3FFF, but got {self.contents.hex()}')
