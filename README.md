# privoxy-dsm
Privoxy package for Synology DSM 6

- Download Privoxy source code into DSM toolkit
<pre>
cd source
wget https://www.privoxy.org/sf-download-mirror/Sources/3.0.26%20%28stable%29/privoxy-3.0.26-stable-src.tar.gz
tar xzf privoxy-3.0.26-stable-src.tar.gz
mv privoxy-3.0.26-stable privoxy
cd privoxy
</pre>

- Get privoxy-dsm folders: synology and SynoBuildConf

- Workaround DSM toolkit missing `group'
<pre>
cp /usr/bin/groups /toolkit/build_env/ds.evansport-6.1/usr/bin
</pre>

- Build for your architecture, example
<pre>
/toolkit/pkgscripts-ng/PkgCreate.py -p evansport -x0 -c privoxy
</pre>

- Install package on Synology from /toolkit/result_spk

- Configure Privoxy on Synology: config files are in /var/packages/privoxy/etc

- TODO: wizard configuration options are non functional for now, need to manually edit config file after install
