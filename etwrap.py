#!/usr/bin/env python

'''
	Get resources and wrap in the eTekkatho HTML
'''

import os

# Main class
class BCWrap():
	'Main class for wrapping resource files in the eTekkatho HTML header and footer'
	
	# Vars
	
	
	# Constructor
	def __init__(self):
		self.getContent()
	
	def getContent(self):
		print('Getting content...')
		
		# Loop through the folders
		rootdir = '../content/'
		
		for subdir, dirs, files in os.walk(rootdir):
				# Add the HTML header
				html = self.getHeader()
				
				#print("Generating page for {}".format(subdir))
				
				for file in files:
					#print(os.path.join(subdir, file))			
					# If folder contains swf add the swf body
					if file.endswith('.swf') and 'framework' not in file and 'assets' not in file:
						# Add the body for flash file
						
						for file2 in files:
							if file2.endswith('.xml'):
								xmlFile = file2
						
						html += """<div style="width: 500px; margin:0 auto"><embed width="500" height="700" flashvars="xmldata={xmlFile}" 
								autoplay="false" wmode="transparent" bgcolor="transparent" 
									pluginspage="http://www.adobe.com/go/getflashplayer" allowScriptAccess="always"
										type="application/x-shockwave-flash" 
											src="{file}" style="display: block;"/></div>""".format(file = file, xmlFile = xmlFile)
						break
						
					# If folder contains mp4 add the mp4 body
					elif file.endswith('.mp4'):
						# Add the body for video file
						
						html += """<video width="800" controls style="width:100%">
									  <source src="{file}" type="video/mp4">
									  Your browser does not support HTML5 video.
									</video>""".format(file = file)
						break
				
				# Add some content
				html += """<h2>Page title</h2>
							<p>
								Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus fringilla metus vel leo convallis volutpat. Nullam ornare, quam id lobortis efficitur, risus quam auctor risus, id interdum ligula justo at elit. Etiam pharetra nulla et hendrerit semper. Mauris nec sapien lacinia, sollicitudin ante nec, lacinia quam. 
							</p>
							"""
				
				# Add the nav links
				html += self.buildNavigation()
				
				# Add the HTML footer
				html += self.getFooter()
				
				# Write the index.html file
				print("Writing index.html file for {}".format(subdir))
				#print(html)
				
				index = open(os.path.join(subdir, "index.html"), "w")
				index.write(html)
				index.close()
				
				if os.path.exists(os.path.join(subdir, "index.html")):
					print('index.html successfully created.')
				else:
					print('index.html does not exist, an error must\'ve occurred.')
				
		print('Done')
	
	def getHeader(self):
		header = """<!doctype html>
						 <html>
						 <head>
							 <!-- css -->
							 <link type="text/css" rel="stylesheet" href="../css/main.css" media="all" />
  							 <link type="text/css" rel="stylesheet" href="../css/style.css" media="all" />
						 </head>
						 <body>
						 <div class="header">
						 <div class="container">
							<p class="skip-link"><a href="#main" class="visuallyhidden focusable">Skip to main content</a></p>
							<div class="site-info">
							  <h1 class="logo"><a href="index.html">eTekkatho</a></h1>
							  <p class="logo-myanmar">
								<a href="/index.html">
									<img src=" data:image/png;base64,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" alt="eTekkatho logo - Myanmar language version" width="139" height="61" />
								</a></p>
							  <h2 class="tagline">Educational resources for the Myanmar academic community</h2>
							</div>
							<div class="nav-primary navbar">
							  <div class="navbar-inner">
								<ul class="nav">
								  <li class="home"><a href="/index.html">Home</a></li>
								  <li class="subjects"><a href="/classifications.html">Subjects</a></li>
								  <li class="search"><a href="/search.html">Search</a></li>
								  <li class="keywords"><a href="/keywords.html">Keywords</a></li>
								  <li class="about"><a href="/about.html">About us</a></li>
								  <li class="help"><a href="/help.html">Help</a></li>
								</ul>
							  </div>
							</div>
							<div class="page-header">
								<a href="/" style="float:right;display:block">British Council home &raquo;</a>
								<img src="../img/bc-logo.jpg" alt="British Council logo" width="200">
							</div>
						  </div>
						</div>
						<div id="main-inner">
						"""
		
		return header
	
	def buildNavigation(self):
		# Build a navigation tree from the file structure
		navHTML = '<div id="footer-nav">'
		rootdir = '../content/'
		
		for subdir, dirs, files in os.walk(rootdir):
			if "css" not in subdir and "img" not in subdir and len(subdir) > 11: 
				subdirname = subdir.replace('_', ': ')
			
				navHTML += """
				<div class="nav-item">
					&raquo; <a href="../{subdir}/index.html">{subdirname}</a>				
				</div>
				""".format(relpath = os.path.relpath(subdir), subdir = subdir.replace("../content/", ""), subdirname = subdirname.replace("../content/", ""))
		
		navHTML += '</div>'
		
		return navHTML
		
	def getFooter(self):
		footer = """</div>
					<div class="footer">
					  <div class="container">
						<p>eTekkatho is hosted and run by The University of Manchester<span class="visuallyhidden">.</span></p>
						<ul class="legal-links">
						  <li><a href="terms-of-service.html">Terms of service</a></li>
						  <li><a href="copyright-licensing.html">Copyright and licensing</a></li>
						</ul>
						<ul class="tribute-logos">
						  <li><img src="../img/university-of-manchester.png" alt="The University of Manchester logo" width="109" height="46" class="tribute-logo" /></li>
						</ul>
					  </div>
					</div>
					
					</body>
					</html>"""
		
		return footer

	
BCWrap()
