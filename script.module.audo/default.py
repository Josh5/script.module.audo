#
import xbmc
import xbmcaddon
import os

__scriptname__ = "audo"
__author__     = "lsellens"
__url__        = "http://code.google.com/p/repository-lsellens/"
__selfpath__   = xbmcaddon.Addon(id='script.module.audo').getAddonInfo('path')

#try to get service addon info or send notification to install it.
try:
    __addon__      = xbmcaddon.Addon(id='script.service.audo')
    __addonpath__  = __addon__.getAddonInfo('path')
    __start__      = xbmc.translatePath(__addonpath__ + '/resources/audo.py')
except:
    xbmc.executebuiltin("XBMC.Notification('audo', 'Install audo service!', '30000', %s)" % ( __selfpath__ + '/icon.png'))
    xbmc.log('AUDO: Could not detect service addon:', level=xbmc.LOGERROR)
    exit()

if __name__ == '__main__':

    # Shutdown audo
    os.system("kill `ps | grep -E 'python.*script.module.audo' | awk '{print $1}'`")

    #Open settings dialog
    __addon__.openSettings()

    # Restart audo
    try:
        xbmc.executebuiltin('XBMC.RunScript(%s)' % __start__, True)
    except Exception, e:
        xbmc.log('AUDO: Could not execute launch script:', level=xbmc.LOGERROR)
        xbmc.log(str(e), level=xbmc.LOGERROR)
