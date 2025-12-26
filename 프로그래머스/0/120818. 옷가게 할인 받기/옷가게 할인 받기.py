def solution(price):
    if(100000 <= price):
        if(300000 <= price):
            if(500000 <= price):
                return int(price * 0.8)
            return int(price * 0.9)
        return int(price * 0.95)
    else:
         return int(price)
        
   