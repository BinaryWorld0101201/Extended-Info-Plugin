from ts3plugin import ts3plugin, PluginHost
import ts3, ts3defines, datetime


class info(ts3plugin):
    name = "Extended Info"
    apiVersion = 20
    requestAutoload = True
    version = "0.1"
    author = "Bluscream"
    description = "Shows you more informations.\nBest to use together with a Extended Info Theme.\n\nCheck out https://r4p3.net/forums/plugins.68/ for more plugins."
    offersConfigure = False
    commandKeyword = ""
    infoTitle = ""
    menuItems = [(ts3defines.PluginMenuType.PLUGIN_MENU_TYPE_GLOBAL, 0, "Extended Info -> Toggle Colors", "icon.png"),(ts3defines.PluginMenuType.PLUGIN_MENU_TYPE_GLOBAL, 1, "Extended Info -> Toggle Meta", "icon.png")]
    hotkeys = []
    colored = False
    meta = False


    def __init__(self):
        ts3.printMessageToCurrentTab('[{:%Y-%m-%d %H:%M:%S}]'.format(datetime.datetime.now())+" [color=orange]"+self.name+"[/color] Plugin for pyTSon by [url=https://github.com/Bluscream]Bluscream[/url] loaded.")

    def onMenuItemEvent(self, schid, atype, menuItemID, selectedItemID):
        if menuItemID == 0:
            info.colored = not info.colored
            ts3.printMessageToCurrentTab('[{:%Y-%m-%d %H:%M:%S}] '.format(datetime.datetime.now())+" Set Colored Infos to [color=yellow]"+str(autoCommander.toggle)+"[/color]")
        elif menuItemID == 1:
            info.meta = not info.meta
            ts3.printMessageToCurrentTab('[{:%Y-%m-%d %H:%M:%S}] '.format(datetime.datetime.now())+" Set Meta Data to [color=yellow]"+str(autoCommander.toggle)+"[/color]")

    def infoData(cls, schid, id, atype):
        i = []
        schid = ts3.getCurrentServerConnectionHandlerID()
        if atype == 0:
            i.append('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
            i.append('Type: [b]Server[/b]')
            i.append("Server Connection Handler ID: "+str(schid))
            #ts3.requestServerVariables(schid)
            (error, id) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_ID)
            if error == ts3defines.ERROR_ok:
                i.append("Virtualserver ID: "+id)
            (error, mid) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_MACHINE_ID)
            if error == ts3defines.ERROR_ok:
                i.append("Machine ID: "+mid)
            (error, uid) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerProperties.VIRTUALSERVER_UNIQUE_IDENTIFIER)
            if error == ts3defines.ERROR_ok:
                i.append("Unique ID: "+uid)
            (error, gip) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_IP)
            if error == ts3defines.ERROR_ok:
                i.append("IP: "+gip)
            (error, clid) = ts3.getClientID(schid)
            if error == ts3defines.ERROR_ok:
                (error, ip) = ts3.getConnectionVariableAsString(schid,clid,6)
                if error == ts3defines.ERROR_ok and ip != gip:
                    i.append("Connect IP: "+ip)

            (error, created) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerProperties.VIRTUALSERVER_CREATED)
            if error == ts3defines.ERROR_ok:
                created = datetime.datetime.fromtimestamp(int(created)).strftime('%Y-%m-%d %H:%M:%S')
                i.append("Created: "+str(created))

            (error, mbu) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_MONTH_BYTES_UPLOADED)
            (error, mbd) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_MONTH_BYTES_DOWNLOADED)
            if error == ts3defines.ERROR_ok:
                i.append("Monthly Traffic: Up: [color=blue]"+mbu+"[/color] B | Down: [color=red]"+mbd+"[/color] B")
            (error, tbu) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_TOTAL_BYTES_UPLOADED)
            (error, tbd) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_TOTAL_BYTES_DOWNLOADED)
            if error == ts3defines.ERROR_ok:
                i.append("Total Traffic: Up: [color=darkblue]"+tbu+"[/color] B | Down: [color=firebrick]"+tbd+"[/color] B")
            (error, tpt) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_TOTAL_PACKETLOSS_TOTAL)
            (error, tpk) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_TOTAL_PACKETLOSS_KEEPALIVE)
            (error, tpc) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_TOTAL_PACKETLOSS_CONTROL)
            (error, tps) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_TOTAL_PACKETLOSS_SPEECH)
            if error == ts3defines.ERROR_ok:
                i.append("Loss Total: [color=magenta]"+tpt+"[/color]% | Keepalive: [color=magenta]"+tpk+"[/color]% | Control: [color=magenta]"+tpc+"[/color]% | Speech: [color=magenta]"+tps+"[/color]%")
            (error, ping) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_TOTAL_PING)
            if error == ts3defines.ERROR_ok:
                i.append("Ping: "+ping+"ms")
            (error, icon) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_ICON_ID)
            if error == ts3defines.ERROR_ok:
                i.append("Icon ID: "+icon)
            (error, aptr) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_ANTIFLOOD_POINTS_TICK_REDUCE)
            if error == ts3defines.ERROR_ok:
                i.append("Points per tick: "+aptr)
            (error, apncb) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_ANTIFLOOD_POINTS_NEEDED_COMMAND_BLOCK)
            if error == ts3defines.ERROR_ok:
                i.append("Points to block commands: "+apncb)
            (error, apnib) = ts3.getServerVariableAsString(schid, ts3defines.VirtualServerPropertiesRare.VIRTUALSERVER_ANTIFLOOD_POINTS_NEEDED_IP_BLOCK)
            if error == ts3defines.ERROR_ok:
                i.append("Points to block IP: "+apnib)
            return i
        elif atype == 1:
            i.append('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
            i.append('Type: [b]Channel[/b]')
            (error, phonick) = ts3.getChannelVariableAsString(schid, id, ts3defines.ChannelPropertiesRare.CHANNEL_NAME_PHONETIC)
            if error == ts3defines.ERROR_ok and phonick != "":
                i.append("Phonetic Nickname: "+phonick)
            (error, icon) = ts3.getChannelVariableAsString(schid, id, ts3defines.ChannelPropertiesRare.CHANNEL_ICON_ID)
            if error == ts3defines.ERROR_ok and icon != "0":
                i.append("Icon ID: "+icon)
            (error, forcedsilence) = ts3.getChannelVariableAsInt(schid, id, ts3defines.ChannelPropertiesRare.CHANNEL_FORCED_SILENCE)
            if error == ts3defines.ERROR_ok:
                if forcedsilence == 1:
                    i.append("Forced Silence: [color=red]YES[/color]")
                else:
                    i.append("Forced Silence: [color=green]NO[/color]")
            (error, private) = ts3.getChannelVariableAsString(schid, id, ts3defines.ChannelPropertiesRare.CHANNEL_FLAG_PRIVATE)
            if error == ts3defines.ERROR_ok:
                if private == 1:
                    i.append("Private Channel: [color=red]YES[/color]")
                else:
                    i.append("Private Channel: [color=green]NO[/color]")
            (error, latency) = ts3.getChannelVariableAsString(schid, id, ts3defines.ChannelProperties.CHANNEL_CODEC_LATENCY_FACTOR)
            if error == ts3defines.ERROR_ok:
                i.append("Latency Factor: "+latency)
            (error, salt) = ts3.getChannelVariableAsString(schid, id, ts3defines.ChannelProperties.CHANNEL_SECURITY_SALT)
            if error == ts3defines.ERROR_ok and salt != "":
                i.append("Security Salt: "+salt)
            (error, pwd) = ts3.getChannelVariableAsString(schid, id, ts3defines.ChannelProperties.CHANNEL_PASSWORD)
            if error == ts3defines.ERROR_ok and pwd != "" and pwd != "dummy":
                i.append("Password: "+pwd)
            (error, filepath) = ts3.getChannelVariableAsString(schid, id, ts3defines.ChannelPropertiesRare.CHANNEL_FILEPATH)
            if error == ts3defines.ERROR_ok and filepath != "":
                i.append("Filepath: "+filepath)
            return i
        elif atype == 2:
            i.append('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
            #ts3.requestClientVariables(schid, id)#ts3.requestConnectioni(schid, id)
            (error, type) = ts3.getClientVariableAsInt(schid, id, ts3defines.ClientPropertiesRare.CLIENT_TYPE)
            if error == ts3defines.ERROR_ok:
                if type == ts3defines.ClientType.ClientType_NORMAL:
                    i.append('Type: [b]Client[/b]')
                elif type == ts3defines.ClientType.ClientType_SERVERQUERY:
                    i.append('Type: [b]ServerQuery[/b]')
                else:
                    i.append('Type: [b]Unknown ('+str(type)+')[/b]')

            (error, country) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_COUNTRY)
            if error == ts3defines.ERROR_ok:
                #if colored:
                    i.append("Country: [color=darkgreen]"+country+"[/color]")
                #else:
                    #i.append("Country: "+country)
            (error, phonick) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_NICKNAME_PHONETIC)
            if error == ts3defines.ERROR_ok and phonick != "":
                i.append("Phonetic Nick: "+phonick)
            (error, unread) = ts3.getClientVariableAsInt(schid, id, ts3defines.ClientPropertiesRare.CLIENT_UNREAD_MESSAGES)
            if error == ts3defines.ERROR_ok:
                if unread == 0:
                    i.append("No unread offline messages.")
                else:
                    i.append("[color=blue][b]"+str(unread)+"[/b][/color] unread offline messages")
            (error, icon) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_ICON_ID)
            if error == ts3defines.ERROR_ok and icon != "0":
                i.append("Icon ID: "+icon)
            (error, tp) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_TALK_POWER)
            if error == ts3defines.ERROR_ok:
                i.append("Talk Power: "+tp)
            (error, avatar) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_FLAG_AVATAR)
            if error == ts3defines.ERROR_ok and avatar != "":
                i.append("Avatar Flag: "+avatar)
            (error, cgid) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_CHANNEL_GROUP_ID)
            if error == ts3defines.ERROR_ok:
                i.append("Channel Group: "+cgid)
            (error, sgids) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_SERVERGROUPS)
            if error == ts3defines.ERROR_ok:
                i.append("Server Groups: "+sgids)
            (error, sqnvp) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_NEEDED_SERVERQUERY_VIEW_POWER)
            if error == ts3defines.ERROR_ok:
                i.append("Needed SQ View Power: "+sqnvp)
            (error, clb) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_BADGES)
            if error == ts3defines.ERROR_ok and clb != "Overwolf=0":
                i.append("Badges: "+clb)
            (error, mmbu) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_MONTH_BYTES_UPLOADED)
            (error, mmbd) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_MONTH_BYTES_DOWNLOADED)
            if error == ts3defines.ERROR_ok and mmbu != "0" and mmbd != "0":
                i.append("Monthly Traffic: Up: [color=blue]"+mmbu+"[/color] B | Down: [color=red]"+mmbd+"[/color] B")
            (error, tmbu) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_TOTAL_BYTES_UPLOADED)
            (error, tmbd) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientPropertiesRare.CLIENT_TOTAL_BYTES_DOWNLOADED)
            if error == ts3defines.ERROR_ok and tmbu != "0" and tmbd != "0":
                i.append("Total Traffic: Up: [color=darkblue]"+tmbu+"[/color] B | Down: [color=firebrick]"+tmbd+"[/color] B")
            (error, version) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientProperties.CLIENT_VERSION)
            if error == ts3defines.ERROR_ok:
                i.append("Version: "+version)
            if info.meta:
                (error, meta) = ts3.getClientVariableAsString(schid, id, ts3defines.ClientProperties.CLIENT_META_DATA)
                if error == ts3defines.ERROR_ok and meta != "":
                    i.append("Meta Data: "+meta)
            return i
        else:
            return ["ItemType \""+str(atype)+"\" unknown."]
