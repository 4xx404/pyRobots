class bc:
	GC = '\033[1;39m'
	BC = '\033[1;34m'
	RC = '\033[1;31m'

class sd:
	iBan = bc.BC + " [" + bc.GC + "?" + bc.BC + "]"
	sBan = bc.BC + " [" + bc.GC + u'\u2713' + bc.BC + "]"
	eBan = bc.BC + " [" + bc.RC + u'\u2717' + bc.BC + "]"
	
	quick = sBan + ' Scan Type: ' + bc.GC + 'Quick'
	extended = sBan + ' Scan Type: ' + bc.GC + 'Directory'
	extendedChoiceBanner = bc.BC + ' Brute Force Directories[' + bc.GC + 'y' + bc.BC + '/' + bc.GC + 'n' + bc.BC + ']: ' + bc.GC
	
	class banner:
		author = bc.BC + "\n Author: " + bc.RC + "4" + bc.GC + "x" + bc.BC + "x" + bc.RC + "4" + bc.GC + "0" + bc.BC + "4\n"
		version = bc.BC + " Version: " + bc.RC + "2" + bc.GC + "." + bc.BC + "0\n"
		github = bc.BC + " Github: " + bc.RC + "h" + bc.GC + "t" + bc.BC + "t" + bc.RC + "p" + bc.GC + "s" + bc.BC + ":" + bc.RC + "/" + bc.GC + "/" + bc.BC + "g" + bc.RC + "i" + bc.GC + "t" + bc.BC + "h" + bc.RC + "u" + bc.GC + "b" + bc.BC + "." + bc.RC + "c" + bc.GC + "o" + bc.BC + "m" + bc.RC + "/" + bc.GC + "4" + bc.BC + "x" + bc.RC + "x" + bc.GC + "4" + bc.BC + "0" + bc.RC + "4\n"

		logo = bc.RC + '''
		               ___       __        __     
		''' + bc.GC + '''    ___  __ __/ _ \___  / /  ___  / /____ 
		''' + bc.BC + '''   / _ \/ // / , _/ _ \/ _ \/ _ \/ __(_-< 
		''' + bc.RC + '''  / .__/\_, /_/|_|\___/_.__/\___/\__/___/ 
		''' + bc.GC + ''' /_/   /___/                              
		''' + author + version + github
		
class menu:
	helper = sd.iBan + ' Include ' + bc.GC + 'http://' + bc.BC + ' | ' + bc.GC + 'https://' + bc.BC + ' in URL'
