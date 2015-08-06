LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_MODULE := F-Droid
LOCAL_MODULE_TAGS := optional
LOCAL_PACKAGE_NAME := F-Droid
LOCAL_SRC_FILES := FDroid.apk

LOCAL_PRIVILEGED_MODULE := true
LOCAL_CERTIFICATE := PRESIGNED

LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)

FDROID_ROOT := $(LOCAL_PATH)

$(FDROID_ROOT)/$(LOCAL_SRC_FILES):
				cd $(FDROID_ROOT) && bash get-prebuilt

include $(BUILD_PREBUILT)

