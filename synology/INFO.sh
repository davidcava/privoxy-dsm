#!/bin/sh
# Copyright (c) 2018-2024 David Cavallini

. /pkgscripts-ng/include/pkg_util.sh

package="privoxy"
version="3.0.34-1"
os_min_ver="7.0-40000"
displayname="Privoxy"
arch="$(pkg_get_platform_family)"
maintainer="David Cavallini"
distributor="davidcava"
distributor_url="https://github.com/davidcava/"
support_url="https://github.com/davidcava/privoxy-dsm/wiki"
description="Privoxy package for Synology DSM7."
description_fre="Paquet Privoxy pour Synology DSM7."
startable="yes"
ctl_stop="yes"
silent_install="yes"
silent_upgrade="yes"
silent_uninstall="yes"
precheckstartstop="no"
silent_install="yes"
silent_upgrade="yes"
silent_uninstall="yes"
dsmuidir="ui"
dsmappname=SYNO.SDS.Privoxy.Application

[ "$(caller)" != "0 NULL" ] && return 0

pkg_dump_info
