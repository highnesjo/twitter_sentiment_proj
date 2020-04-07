from textblob import TextBlob
import xlrd 


loc = ("data.xlsx") 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
r = sheet.nrows
tws = []

for k in range(1,r):
	v = sheet.cell_value(k, 1)
	sp = (TextBlob(v).sentiment.polarity)
	tws.append([k,v,sheet.cell_value(k, 3),sp])

class airlinesentiment:
	p = 0
	n = 0

va = airlinesentiment()
united = airlinesentiment()
southwest = airlinesentiment()
delta = airlinesentiment()
ua = airlinesentiment()
american = airlinesentiment()
	
for q in tws:
	if q[2] == 'Virgin America':
		if q[3] >= 0:
			va.p = va.p+1
		else:
			va.n = va.n+1

	elif q[2] == 'United':
		if q[3] >= 0:
			united.p = united.p+1
		else:
			united.n = united.n+1

	elif q[2] == 'Southwest':
		if q[3] >= 0:
			southwest.p = southwest.p+1
		else:
			southwest.n = southwest.n+1

	elif q[2] == 'Delta':
		if q[3] >= 0:
			delta.p = delta.p+1
		else:
			delta.n = delta.n+1

	elif q[2] == 'US Airways':
		if q[3] >= 0:
			ua.p = ua.p+1
		else:
			ua.n = ua.n+1

	elif q[2] == 'American' :
		if q[3] >= 0:
			american.p = american.p+1
		else:
			american.n = american.n+1

	else:
		print("Criteria not matched")


print("Virgin America -> ","Positive",va.p,"Negative",va.n)
print("United -> ","Positive",united.p,"Negative",united.n)
print("Southwest -> ","Positive",southwest.p,"Negative",southwest.n)
print("Delta -> ","Positive",delta.p,"Negative",delta.n)
print("US Airways -> ","Positive",ua.p,"Negative",ua.n)
print("American -> ","POsitive",american.p,"Negative",american.n)
