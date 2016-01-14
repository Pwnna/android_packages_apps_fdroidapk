#!/usr/bin/env python
from __future__ import print_function

import urllib
import urllib2
import sys
import os

META_URL_PREFIX = "https://gitlab.com/fdroid/fdroiddata/raw/master/metadata"


class PackageNotFound(Exception):
  pass


def meta_url(package_name):
  return META_URL_PREFIX + "/" + package_name + ".txt"


def log(msg):
  print("[fdroid] {}".format(msg))


def get_latest_version(package_name):
  try:
    response = urllib2.urlopen(meta_url(package_name))
  except urllib2.HTTPError as e:
    if e.code == 404:
      raise PackageNotFound("{} cannot be found at {}".format(package_name, meta_url(package_name)))
    else:
      raise

  for line in response:
    line = line.strip()
    if line.startswith("Current Version Code"):
      return int(line.split(":")[1])


def apk_url(package_name, version_code):
  return "https://f-droid.org/repo/{}_{}.apk".format(package_name, version_code)


def download_package(package_name, version_code):
  urllib.urlretrieve(apk_url(package_name, version_code), package_name + ".apk")


def main(argv):
  package_name = argv[0]
  log("getting latest version code")
  version_code = get_latest_version(package_name)
  log("latest version code is: {}".format(version_code))

  last_modified_filename = package_name + ".last-version"
  if os.path.exists(last_modified_filename):
    with open(last_modified_filename) as f:
      current_version_code = int(f.read().strip())

    log("last version is: {}".format(current_version_code))
  else:
    current_version_code = float("-inf")

  if version_code > current_version_code:
    with open(last_modified_filename, "w") as f:
      f.write(str(version_code))

    local_filename = package_name + ".apk"
    if os.path.exists(local_filename):
      os.remove(local_filename)

    log("new version detected... downloading...")
    download_package(package_name, version_code)
    log("downloaded")


if __name__ == "__main__":
  main(sys.argv[1:])

