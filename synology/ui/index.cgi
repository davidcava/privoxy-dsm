#!/bin/sh

#This CGI script calls http://config.privoxy.org through Privoxy HTTP proxy rewriting the URLs both ways

PRIVOXY_URI="http://config.privoxy.org"

URL_PATH=`expr match "$REQUEST_URI" '.*'"$SCRIPT_NAME"'/\(.*\)'`

#uncomment to debug error pages returned by Privoxy CGI admin pages
#echo "Status: 200 OK"
#echo "Content-type: text/plain"
#echo 

# Check authentication as administrative user
SYNOTOKEN=$(/usr/syno/synoman/webman/login.cgi | sed 's/
user=$(QUERY_STRING="SynoToken=$SYNOTOKEN" /usr/syno/synoman/webman/modules/authenticate.cgi)
if [ "$user" != "admin" ]
then
    echo 
    echo "<HTML><HEAD><TITLE>Login Required</TITLE></HEAD><BODY>Please login as admin first, before using this webpage ()</BODY></HTML>"
    exit 0
fi

curl -q -i -s --referer "$PRIVOXY_URI/" --user-agent "Synology DSM" --proxy "http://127.0.0.1:8118" "$PRIVOXY_URI/$URL_PATH" | sed -e 's~href=\"/~href=\"'"$SCRIPT_NAME/"'~g' -e 's~href=\"'"$PRIVOXY_URI"'~href=\"'"$SCRIPT_NAME"'~g' 2>&1

#uncomment to debug Synology CGI environment variables
#echo "<PRE>"
#echo "url_path=$URL_PATH"
#env
#echo "</PRE>"

exit 0
