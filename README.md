# privoxy-dsm
Synology DSM packages for Privoxy.

# Installation
Download the spk for your architecture from the [Release](https://github.com/davidcava/privoxy-dsm/releases) section, then install using Synology Package Center button _Manual Install_. See  architectures on [Synology knowledge base](https://www.synology.com/en-us/knowledgebase/DSM/tutorial/General/What_kind_of_CPU_does_my_NAS_have).

# Usage
Privoxy on Synology can be used:
- As the filtering proxy it is normally meant to be (default setup),
- Or as a neutral HTTP/HTTPS proxy that forwards requests through a SOCKS proxy for your other Synology apps (SickChill, Radarr, Sonarr, CouchPotato...).

You need to manually adapt the Privoxy config file installed in /var/packages/privoxy/etc/config accordingly (through SSH).
Especially, change listen address to 0.0.0.0 if you wish to use the proxy not only from your Synology applications. In this case you also need to open the port 8118 in Synology firewall.
You might also want to uncomment the 4 debug options to get some logs in /var/packages/privoxy/var/logfile (this log file can also be viewed from the Package Center).
Except when changing the listen address, config changes are normally immediately taken into account without needing to stop/start privoxy. 

Your modifications in `config` file are preserved in case of package uninstallation/reinstallation or upgrade. When a modified config file already exists, the installer will install instead `config.new` in same folder. Same for user.action, user.filter, match-all.action and trust, as those 4 files are meant to be personalized. On the other hand default.action and default.filter are silently overwritten.

Additionaly to the [normal Privoxy way](https://www.privoxy.org/user-manual/configuration.html), the Privoxy admin page can also be opened from within DSM by clicking on the Privoxy icon when authenticated as a user who is an administrator. This allows to use the admin pages even when the proxy is not accessible from outside the Synology machine (when it listens on 127.0.0.1 or firewall port 8118 is kept closed).

# Limitation
Just after installing, clicking on the icon might not launch the Privoxy admin page as expected. Workaround is to reload the Synology web page and retry.

Branch master works on DSM 7.
Branch dsm6 works on DSM 6.1 and 6.2 (not maintained anymore, binaries until 3.0.32-2).

Since DSM7, after installing the package, opening the admin page from within DSM needs to manually ssh into the Synology and run: sudo /var/packages/privoxy/scripts/addprivileges. It is not strictly necessary though as privoxy still works without this.

Listening port should be left as default (8118) (changing it probably breaks admin pages and maybe other things).

No setup wizard so you need to manually edit the config file after install if the default config does not suit you.

# Build from source
- Setup the DSM toolkit for your model according to the official Synology [Developer's guide](https://global.download.synology.com/download/Document/Software/DeveloperGuide/Os/DSM/All/enu/DSM_Developer_Guide_7_enu.pdf)
- Download Privoxy source code into the toolkit
  ```sh
  cd source
  wget https://www.privoxy.org/sf-download-mirror/Sources/3.0.34%20%28stable%29/privoxy-3.0.34-stable-src.tar.gz
  tar xzf privoxy-3.0.34-stable-src.tar.gz
  mv privoxy-3.0.34-stable privoxy
  cd privoxy
  ```
- Add or link the 2 subfolders `synology` and `SynoBuildConf` from `privoxy-dsm` into the privoxy source folder
  ```sh
  git clone https://github.com/davidcava/privoxy-dsm.git
  ln -s ./privoxy-dsm/SynoBuildConf ./privoxy-dsm/synology .
  ```
- Build for your architecture (or for several), example
  ```sh
  /toolkit/pkgscripts-ng/PkgCreate.py -v7.0 -x0 -c privoxy --print-log -p "evansport broadwell alpine qoriq rtd1296 comcerto2k armada370 armada375 armadaxp monaco armada38x hi3535"
  ```
- If everything went fine, package is now in `/toolkit/result_spk`

# Licence
    Copyright (c) 2018-2021 David Cavallini

    privoxy-dsm is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.
    
    Binary (spk) packages in Release area combine files from Privoxy and privoxy-dsm.
    The applicable licence for those spk files is GPL v2, to comply with Privoxy licence.

    privoxy-dsm is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with privoxy-dsm.  If not, see <http://www.gnu.org/licenses/>.
