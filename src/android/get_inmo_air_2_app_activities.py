import subprocess

# List of package names to query
package_names = [
    "com.android.providers.telephony", "com.sprd.engineermode", "com.android.providers.calendar",
    "com.android.providers.media", "com.sprd.firewall", "com.android.documentsui",
    "android.auto_generated_rro__", "com.android.externalstorage", "com.android.htmlviewer",
    "com.android.companiondevicemanager", "com.android.mms.service", "com.sprd.omacp",
    "com.android.providers.downloads", "com.discord", "com.android.sprd.telephony.server",
    "com.android.browser", "com.arglasses.appstore", "com.android.soundrecorder",
    "com.android.defcontainer", "com.android.vending", "com.android.pacprocessor",
    "com.android.simappdialog", "com.sprd.validationtools", "com.arglasses.settings",
    "com.arglasses.documents", "com.android.certinstaller", "com.android.carrierconfig",
    "android", "com.android.camera2", "com.arglasses.camera",
    "cn.wps.moffice_eng.xiaomi.lite", "com.android.mtp", "com.android.stk",
    "com.android.backupconfirm", "com.arglasses.btservice", "com.android.provision",
    "com.android.statementservice", "com.unisoc.storageclearmanager", "com.android.messaging.smilplayer",
    "com.android.settings.intelligence", "com.android.calendar", "com.arglasses.ota",
    "com.extend.coolclean", "com.android.providers.settings", "com.android.sharedstoragebackup",
    "com.android.webview", "com.android.se", "com.android.inputdevices",
    "com.whispercppdemo", "com.android.musicfx", "com.android.mmsfolderview",
    "com.sprd.autoslt", "com.apowersoft.mirror.tv", "android.ext.shared",
    "com.sprd.uplmnsettings", "com.android.server.telecom", "com.android.keychain",
    "com.arglasses.controlcenter", "com.sprd.uasetting", "com.android.dialer",
    "com.android.gallery3d", "com.spreadtrum.ims", "com.spreadtrum.vce",
    "com.google.android.gms", "com.google.android.gsf", "android.ext.services",
    "com.android.calllogbackup", "com.android.packageinstaller", "com.android.carrierdefaultapp",
    "tranzi.ai.wear", "com.arglasses.launcher", "com.android.proxyhandler",
    "com.inmolens.inmocommunicatetranslate", "com.sprd.logmanager", "com.arglasses.txtreader",
    "com.baidu.map.location", "com.android.storagemanager", "com.android.settings",
    "com.spreadtrum.sgps", "com.unisoc.tui", "com.arglasses.album",
    "com.simplemobiletools.voicerecorder", "com.inmo.inputmethod.pinyin", "com.android.vpndialogs",
    "com.android.music", "com.android.phone", "com.android.shell",
    "com.android.providers.blockednumber", "com.android.providers.userdictionary", "com.android.emergency",
    "com.android.location.fused", "com.android.deskclock", "com.android.systemui",
    "com.android.bluetoothmidiservice", "com.android.bluetooth", "com.arglasses.arservice",
    "com.android.providers.contacts", "com.android.captiveportallogin"
]

# Function to run adb command and capture output
def get_package_info(package_name):
    try:
        result = subprocess.check_output(
            f"adb shell dumpsys package {package_name} | grep -i activity", shell=True
        ).decode('utf-8')
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error querying package {package_name}: {e}")
        return None


# Iterate over package names, get info, and add to list if activity info is present
for package in package_names:
    print(package)
    output = get_package_info(package)
    print(output)
# Print the list of packages with activity information
print("End")
