atm=[["emma","gjflvnmju764",87654],
     ["john","njdvbhfjsak",103446],
     ["claire","dhfwnbssj",963837]    
    ]

def checkBalance(id):
    for i in atm:
        if i[1]==id:
            print(i[2])

checkBalance("dhfwnbssj")