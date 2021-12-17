from build_kernel.utils.device import register_device
from device.xiaomi.sdm660 import XiaomiSDM660Device

class XiaomiJasmine_SproutDevice(XiaomiSDM660Device):
	  PRODUCT_DEVICE = "jasmine_sprout"
	  TARGET_KERNEL_CONFIG = f"vendor/{PRODUCT_DEVICE}_defconfig"
 	  AB_OTA_UPDATER = True
register_device(XiaomiJasmine_SproutDevice)
