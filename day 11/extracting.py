original_dict={'name':'divya','age':58,'city':'madurai','job':'engineer','salary':60000}
key=['age','job']
dict={j:original_dict[j]for j in key if j in original_dict}
print(dict)
