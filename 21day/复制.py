f_n = input("输入字")
o_n = open(f_n,"r")
#content = o_n.read()
position = f_n.rfind(".")
n_f_n = f_n[0:position]+"复制"+f_n[position:]
a = open(n_f_n,"w")
while True:
	content = o_n.read(10)
	if len(content) == 0:
		break
	a.write(content)
o_n.close
a.close
