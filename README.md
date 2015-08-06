FDroid in CM
============

This repository allows you to build FDroid into CyanogenMod and allow it to
automatically install into /system/priv-app, allowing it to upgrade/remove
apps without prompting the user.

To use
------

While inside CyanogenMod 12.1 source directory:

    $ cd .repo/local_manifests
    $ wget -O fdroidapk.xml https://raw.githubusercontent.com/Pwnna/android_packages_apps_fdroidapk/cm-12.1/local_manifest.xml
    $ croot
    $ repo sync

This should put this into packages/apps/FDroid, and should include the
latest FDroid in your ROM!

Now we need to add to all devices:

    $ croot
    $ mkdir -p vendor/extra
    $ echo "PRODUCT_PACKAGES += F-Droid" > vendor/extra/product.mk

