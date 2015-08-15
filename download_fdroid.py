#!/usr/bin/env python
from __future__ import print_function

from email.utils import parsedate
from datetime import datetime
import os
import sys
import urllib
import urllib2


LAST_MODIFIED_FILE = "fdroid-last-modified"
FDROID_APK_URL = "https://f-droid.org/FDroid.apk"
FDROID_APK_PATH = "F-Droid.apk"


def head_request(url):
  req = urllib2.Request(url)
  req.get_method = lambda: "HEAD"

  resp = urllib2.urlopen(req)
  return resp


def parse_http_date(http_date):
  return datetime(*parsedate(http_date)[:6])


def log(msg):
  print("[fdroid] {}".format(msg))


def main():
  log("checking if apk needs to be updated")
  resp = head_request(FDROID_APK_URL)
  if resp.code != 200:
    print("error: unable to send HEAD request to F-Droid:", resp.code, file=sys.stderr)
    sys.exit(1)

  last_modified = resp.info().get("Last-Modified")
  if last_modified is None:
    print("error: unable to get last modified from F-Droid, please update this script", file=sys.stderr)
    sys.exit(1)

  log("server last updated: {}".format(last_modified))

  last_modified_server = parse_http_date(last_modified)

  should_replace = False
  if os.path.exists(LAST_MODIFIED_FILE):
    with open(LAST_MODIFIED_FILE) as f:
      last_modified_local_string = f.read()
      last_modified_local = parse_http_date(last_modified_local_string)
      log("local last updated: {}".format(last_modified_local_string))
      if last_modified_server > last_modified_local:
        should_replace = True
  else:
    log("no local apk detected")
    should_replace = True

  with open(LAST_MODIFIED_FILE, "w") as f:
    f.write(last_modified)

  if should_replace:
    log("redownloading fdroid apk")
    if os.path.exists(FDROID_APK_PATH):
      os.remove(FDROID_APK_PATH)

    urllib.urlretrieve(FDROID_APK_URL, FDROID_APK_PATH)
    log("fdroid downloaded")

if __name__ == "__main__":
  main()

#!/bin/bash

# if [ ! -f FDroid.apk ]; then
#   echo "Downloading F-Droid..."
#   wget -O FDroid.apk https://f-droid.org/FDroid.apk
# else
#   echo "Skipping F-Droid download... already exists."
# fi

