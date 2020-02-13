def gen_pdf(file_name,content):
	
	f = open(file_name, "w")
	f.write(content)
	f.close()

gen_pdf("simple_demo.pdf","ok")