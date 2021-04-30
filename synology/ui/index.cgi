#!/bin/sh
# Copyright (c) 2018-2021 David Cavallini
#    This file is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    It is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this file.  If not, see <http://www.gnu.org/licenses/>.

#This CGI script calls http://config.privoxy.org through Privoxy HTTP proxy rewriting the URLs both ways

PRIVOXY_URI="http://config.privoxy.org"
PRIVOXY_URI_MATCH="https?://config.privoxy.org"
PRIVOXY_PORT=8118
LOG_FILE="/var/packages/privoxy/target/var/log/privoxy/privoxy-dsm.log"

URL_PATH=`expr match "$REQUEST_URI" '.*'"$SCRIPT_NAME"'/\(.*\)'`

#uncomment to debug error pages returned by Privoxy CGI admin pages
#echo "Status: 200 OK"
#echo "Content-type: text/plain"
#echo 

# Check authentication as administrative user
#SYNOTOKEN=$(/usr/syno/synoman/webman/login.cgi | sed -E -n '/^\x0D?$/,$p' | jq -r '.SynoToken') # more robust: real JSON parsing of the response body
SYNOTOKEN=$(/usr/syno/synoman/webman/login.cgi | sed -n '/"SynoToken"/s/^.*"SynoToken".*:.*"\(.*\)".*$/\1/p') # simpler: just sed
if ! user=$(QUERY_STRING="SynoToken=$SYNOTOKEN" /usr/syno/synoman/webman/modules/authenticate.cgi) \
    || [ "$user" = "" ] \
    || ! id -G -n "$user" | grep -q "\<administrators\>"
then
    echo 
    echo "<HTML><HEAD><TITLE>Login Required</TITLE></HEAD><BODY>Please login with admin rights before using this page</BODY></HTML>"
    exit 0
fi

curl -q -i -s --referer "$PRIVOXY_URI/" --user-agent "Synology DSM" --proxy "http://127.0.0.1:$PRIVOXY_PORT" "$PRIVOXY_URI/$URL_PATH" | sed -E -e 's~href=\"/~href=\"'"$SCRIPT_NAME/"'~g' -e 's~'"$PRIVOXY_URI_MATCH"'~'"$SCRIPT_NAME"'~g' 2>>LOG_FILE # | tee -a /var/packages/privoxy/target/var/log/privoxy/responses.log

#uncomment to debug Synology CGI environment variables
#echo "<PRE>"
#echo "url_path=$URL_PATH"
#env
#echo "</PRE>"

exit 0

