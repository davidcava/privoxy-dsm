# privoxy-dsm
Privoxy package for Synology DSM 6

# Installation

Download the spk for your architecture from the release section, then install from Package Center with button _Manual Install_. See  architectures on [Synology knowledge base](https://www.synology.com/en-us/knowledgebase/DSM/tutorial/General/What_kind_of_CPU_does_my_NAS_have).

# Limitation
The package is designed and built for DSM 6.1.

It will probably not install or work on earlier DSM versions.
It might work on more recent DSM versions but I have not tested.
Listening port should be left as default (8118) (changing it probably breaks admin pages and maybe other things).

# Usage

Privoxy on Synology can be used:
- As the filtering proxy it is normally meant to be (default setup),
- Or as a neutral HTTP/HTTPS proxy that forwards requests through a SOCKS proxy for your other Synology apps (SickRage, CouchPotato...).

Adapt the Privoxy config file installed in /var/packages/privoxy/etc/config accordingly.
Especially, change listen address to 0.0.0.0 if you wish to use the proxy not only from your Synology applications. In this case you also need to open the port 8118 in Synology firewall.

Modifications in `config` file will be preserved in case of package uninstallation/reinstallation or upgrade. When a modified config file already exists, the installer will put instead `config.new` in same folder.

# Build from source

- Download Privoxy source code into DSM toolkit
```sh
cd source
wget https://www.privoxy.org/sf-download-mirror/Sources/3.0.26%20%28stable%29/privoxy-3.0.26-stable-src.tar.gz
tar xzf privoxy-3.0.26-stable-src.tar.gz
mv privoxy-3.0.26-stable privoxy
cd privoxy
```
- Get privoxy-dsm folders `synology` and `SynoBuildConf`
- Workaround DSM toolkit missing `group`
```sh
cp /usr/bin/groups /toolkit/build_env/ds.evansport-6.1/usr/bin
```
- Build for your architecture, example
```sh
/toolkit/pkgscripts-ng/PkgCreate.py -p evansport -x0 -c privoxy
```
- Install package on Synology from `/toolkit/result_spk`
- Configure Privoxy on Synology: config files are in `/var/packages/privoxy/etc`
- TODO: wizard configuration options are non functional for now, need to manually edit config file after install
