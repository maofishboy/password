password = 'a123456'
i=3
while i > 0:
    myPassword = input('請使用者輸入密碼: ')
    if myPassword == password:
        print('密碼成功')
        break
    else:
        i = i - 1
        print('密碼錯誤! ')
        if i > 0:
        	print('還有' ,i,'次機會')
        else:
        	print('沒有機會')
        	

    