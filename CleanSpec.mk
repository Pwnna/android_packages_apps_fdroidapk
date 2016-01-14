$(call add-clean-step, rm -rf packages/apps/FDroid/org.fdroid.fdroid.apk)
$(call add-clean-step, rm -rf packages/apps/FDroid/org.fdroid.fdroid.privileged.apk)
$(call add-clean-step, rm -rf packages/apps/FDroid/org.fdroid.fdroid.privileged.last-version)
$(call add-clean-step, rm -rf packages/apps/FDroid/org.fdroid.fdroid.last-version)
$(call add-clean-step, rm -rf $(PRODUCT_OUT)/obj/APPS/F-Droid_intermediates)

