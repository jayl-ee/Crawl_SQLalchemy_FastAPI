''' 
딕셔너리 형식 !! 
JSON 의 열 이름  :  테이블의 열 이름'''

at_dict = {
            "saleDate" : "saleDate",
            "whsalName" : "market_name", 
            'whsalCd' : "market_code",
            'smallName' : "item",
            'minAmt' : "min_price",
            'maxAmt' : "max_price",
            'avgAmt' : "avg_price"
}


weather_dic = {
                "tm" : "date", # 날짜
                "stnId" : "state_id", # 지점코드
                "stnNm" : "state", # 지점명
                "avgTa" : "avg_temp", # 평균기온
                "minTa" : "min_temp", # 최저 기온
                "minTaHrmt" : "min_temp_time", # 최저기온시각
                "maxTa" : "max_temp", # 최고 기온
                "maxTaHrmt" : "max_temp_time", # 최고기온시각
                "sumRnDur" : "rain_dur_time", # 강수 계속시간
                "mi10MaxRn" : "min10_max_rain",  # 10분 최다 강수량          
                "mi10MaxRnHrmt" : "min10_max_rain_time", # 10분 최다 강수량 시각
                "hr1MaxRn" : "hour1_max_rain", # 1시간 최다강수량
                "hr1MaxRnHrmt" : "hour1_max_rain_time", # 1시간 최다강수량 시각
                "sumRn" : "rain_all_day", # 일 강수량
                "maxInsWs" : "max_ins_wind_speed", # 최대 순간 풍속
                "maxInsWsWd" : "max_ins_wind_speed_dir", # 최대 순간 풍속 풍향(16방위)
                "maxInsWsHrmt" : "max_ins_wind_speed_time", # 최대 순간 풍속 시각(hhmi)
                "maxWs" : "max_wind_speed",# 최대 풍속
                "maxWsWd" : "max_wind_speed_dir", # 최대 풍속 풍향(16방위)
                "maxWsHrmt" : "max_wind_speed_time", # 최대 풍속 시각(hhmi)
                "avgWs" : "avg_wind_speed", # 평균풍속
                "hr24SumRws" : "hr24_sum_rws",  # 풍정합
                "maxWd" : "max_wind", # 최다 풍향
                "avgTd" : "ave_dew_point_temp", # 평균 이슬점 온도(c)
                "minRhm" : "min_moisture",  # 최소 상대습도
                "minRhmHrmt" : "min_moisture_time",  # 평균 상대습도 시각
                "avgRhm" : "avg_moisture", # 평균 상대습도
                "avgPv" : "avg_pressure",  # 평균 증기압
                "avgPa" : "avg_pressure_at", # 평균 현지기압
                "maxPs" : "max_pressure_sea",  # 최고 해면 기압
                "maxPsHrmt" : "max_pressure_sea_time", # 최고 해면기압 시각
                "minPs" : "min_pressure_sea", # 최저 해면기압
                "minPsHrmt" : "min_pressure_sea_time", # 최저 해면기압 시각
                "avgPs" : "avg_pressure_sea", # 평균 해면기압
                "ssDur" : "dur_sun", # 가조 시간
                "sumSsHr" : "sum_sun_hour", # 합계 일조 시간
                "hr1MaxIcsrHrmt" : "hr1_max_time", # 1시간 최다 일사 시각
                "hr1MaxIcsr" : "hr1_max_rate", # 1시간 최다 일사량
                "sumGsr" : "sum_sun", # 합계 일사량
                "ddMes" : "day_snow", # 일 최심적설
                "ddMefs" : "day_snow_new", # 일 최심신적설
                "avgTca" : "avg_cloud", # 평균 전운량(10분위)
                "avgTs" : "avg_ground_temp" # 평균 지면온도
        }