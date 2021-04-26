import pyupbit

access  =  "63xxFi3FQydoubQXpPzG7uLXjOmLI1eJnn7r09Go"           # 본인으로 값 변경 
secret  =  "7J3aQVJNXq17Kdx2qPnIv0s7s5VU6Qax2PAPFCmN"           # 본인 값으로 
upbit =  pyupbit.Upbit ( access , secret )

print(upbit.get_balance("KRW-XRP")) # KRW-XRP 조회
print(upbit.get_balance("KRW")) # 보유 현금 조회