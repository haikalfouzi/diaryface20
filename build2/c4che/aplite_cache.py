AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'aplite'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'aplite'
BUNDLE_NAME = 'pebble.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_APLITE', 'PBL_BW', 'PBL_RECT', 'PBL_COMPASS', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
INCLUDES = ['aplite']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {}
MESSAGE_KEYS_HEADER = '/pebble/build/include/message_keys.auto.h'
NODE_PATH = '/home/pebble/.pebble-sdk/SDKs/current/node_modules'
PEBBLE_SDK_COMMON = '/home/pebble/.pebble-sdk/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/home/pebble/.pebble-sdk/SDKs/current/sdk-core/pebble/aplite'
PEBBLE_SDK_ROOT = '/home/pebble/.pebble-sdk/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['aplite', 'bw', 'rect', 'compass', '144w', '168h'], 'MAX_FONT_GLYPH_SIZE': 256, 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 524288, 'MAX_APP_MEMORY_SIZE': 24576, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'aplite', 'BUNDLE_BIN_DIR': 'aplite', 'BUILD_DIR': 'aplite', 'MAX_RESOURCES_SIZE_APPSTORE_2_X': 98304, 'MAX_RESOURCES_SIZE_APPSTORE': 131072, 'DEFINES': ['PBL_PLATFORM_APLITE', 'PBL_BW', 'PBL_RECT', 'PBL_COMPASS', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168']}
PLATFORM_NAME = 'aplite'
PREFIX = '/usr/local'
PROJECT_INFO = {u'sdkVersion': u'3', u'projectType': u'native', u'uuid': u'9538bece-9027-4f6f-81b1-a44620085992', u'appKeys': {}, u'companyName': u'Max Baeumle/James Fowler', 'messageKeys': {}, u'targetPlatforms': [u'aplite', u'basalt'], u'capabilities': [u''], u'versionLabel': u'2.7', u'longName': u'Diary Face', u'shortName': u'Diary Face', u'watchapp': {u'watchface': True}, u'resources': {u'media': [{u'type': u'png', u'name': u'PEBBLE', u'file': u'images/pebble.png'}, {u'type': u'png', u'name': u'ENTRY_5', u'file': u'images/entry-5.png'}, {u'type': u'png', u'name': u'ENTRY_4', u'file': u'images/entry-4.png'}, {u'type': u'png', u'name': u'ENTRY_3', u'file': u'images/entry-3.png'}, {u'type': u'png', u'name': u'ENTRY_2', u'file': u'images/entry-2.png'}, {u'type': u'png', u'name': u'ENTRY_0', u'file': u'images/entry-0.png'}, {u'type': u'png', u'name': u'ENTRY_1', u'file': u'images/entry-1.png'}, {u'type': u'png', u'name': u'WATCH_BATTERY_CHARGE_ICON', u'file': u'images/watch-battery-charge.png'}, {u'type': u'png', u'name': u'PHONE_BATTERY_CHARGE_ICON', u'file': u'images/phone-battery-charge.png'}, {u'type': u'font', u'name': u'FONT_ROBOTO_CONDENSED_21', u'file': u'fonts/Roboto-Condensed.ttf'}, {u'type': u'font', u'characterRegex': u'[:0-9]', u'name': u'FONT_ROBOTO_BOLD_SUBSET_49', u'file': u'fonts/Roboto-Bold.ttf'}, {u'type': u'png', u'name': u'WATCH_BATTERY_ICON', u'file': u'images/watch-battery-normal.png'}, {u'type': u'png', u'name': u'PHONE_BATTERY_ICON', u'file': u'images/phone-battery-normal.png'}, {u'type': u'png', u'name': u'IMAGE_STATUS_1', u'file': u'images/status1.png'}, {u'type': u'png', u'name': u'IMAGE_STATUS_2', u'file': u'images/status2.png'}]}}
REQUESTED_PLATFORMS = [u'aplite', u'basalt']
RESOURCES_JSON = [{u'type': u'png', u'name': u'PEBBLE', u'file': u'images/pebble.png'}, {u'type': u'png', u'name': u'ENTRY_5', u'file': u'images/entry-5.png'}, {u'type': u'png', u'name': u'ENTRY_4', u'file': u'images/entry-4.png'}, {u'type': u'png', u'name': u'ENTRY_3', u'file': u'images/entry-3.png'}, {u'type': u'png', u'name': u'ENTRY_2', u'file': u'images/entry-2.png'}, {u'type': u'png', u'name': u'ENTRY_0', u'file': u'images/entry-0.png'}, {u'type': u'png', u'name': u'ENTRY_1', u'file': u'images/entry-1.png'}, {u'type': u'png', u'name': u'WATCH_BATTERY_CHARGE_ICON', u'file': u'images/watch-battery-charge.png'}, {u'type': u'png', u'name': u'PHONE_BATTERY_CHARGE_ICON', u'file': u'images/phone-battery-charge.png'}, {u'type': u'font', u'name': u'FONT_ROBOTO_CONDENSED_21', u'file': u'fonts/Roboto-Condensed.ttf'}, {u'type': u'font', u'characterRegex': u'[:0-9]', u'name': u'FONT_ROBOTO_BOLD_SUBSET_49', u'file': u'fonts/Roboto-Bold.ttf'}, {u'type': u'png', u'name': u'WATCH_BATTERY_ICON', u'file': u'images/watch-battery-normal.png'}, {u'type': u'png', u'name': u'PHONE_BATTERY_ICON', u'file': u'images/phone-battery-normal.png'}, {u'type': u'png', u'name': u'IMAGE_STATUS_1', u'file': u'images/status1.png'}, {u'type': u'png', u'name': u'IMAGE_STATUS_2', u'file': u'images/status2.png'}]
RPATH_ST = '-Wl,-rpath,%s'
SANDBOX = False
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 78
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['emery', 'chalk', 'aplite', 'diorite', 'basalt']
TARGET_PLATFORMS = ['basalt', 'aplite']
TIMESTAMP = 1637687807
USE_GROUPS = True
VERBOSE = 0
WEBPACK = '/home/pebble/.pebble-sdk/SDKs/current/node_modules/.bin/webpack'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
