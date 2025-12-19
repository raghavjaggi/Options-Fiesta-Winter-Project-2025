import numpy as np
import matplotlib.pyplot as plt

def main():
    # accepting input of variables
    k = int(input("Enter strike price: "))
    p = int(input("Enter premium involved (enter a positive value only): "))
    print("Enter spot price range:-")
    ll = int(input("Enter lower limit (if the lower limit is K-50, enter 50): "))
    ul = int(input("Enter upper limit (if the upper limit is K+30, enter 30): "))
    optype = input("Enter type of option (c for call option, p for put option): ")

    # two plots are displayed for call and put choices, showing profit/loss vs spot price from buyer's and sellers's POV
    s = np.linspace(k-ll, k+ul, 500)
    if(optype=="c"):
        profit = np.maximum(s-k, 0) - p
        plt.subplot(1,2,1)
        plt.plot(s, profit, ':r')
        plt.title("Buying a Call Option", size=15)
        plt.xlabel("Spot Price", color='b')
        plt.ylabel("Profit/Loss", color='b')
        plt.grid()

        plt.subplot(1,2,2)
        plt.plot(s, -(profit), ':r')
        plt.title("Selling a Call Option", size=15)
        plt.xlabel("Spot Price", color='b')
        plt.ylabel("Profit/Loss", color='b')
        plt.grid()
    elif(optype=="p"):
        profit = np.maximum(k-s, 0) - p
        plt.subplot(1,2,1)
        plt.plot(s, profit, ':r')
        plt.title("Buying a Put Option", size=15)
        plt.xlabel("Spot Price", color='b')
        plt.ylabel("Profit/Loss", color='b')
        plt.grid()

        plt.subplot(1,2,2)
        plt.plot(s, -(profit), ':r')
        plt.title("Selling a Put Option", size=15)
        plt.xlabel("Spot Price", color='b')
        plt.ylabel("Profit/Loss", color='b')
        plt.grid()

    plt.suptitle("Payoff Curves of Vanilla Options", size=20)
    plt.show()
main()

""" OPTION GREEKS:-
The premium paid in an option is decided by the formula:- premium = intrinsic value(IV) + extrinsic value(time +volatility). 
We use option greeks to calculate the extrinsic value. Greeks are certain factors that help option traders assess risk and potential rewards
when buying an option. They act as a measure of an option's sensitivity to external market factors.
There are 5 main option greeks: delta, gamma, theta, vega, rho:-

1.DELTA(directional risk)- It is defined as the change in the option price/premium wrt underlying price/spot price. eq. for a $! change in 
spot price, if the premium by $0.6, the delta is 0.6. 
Call options have delta in (0, 1) range(as if s increases, profit wud increase, so to compensate, the premium shud also increase).
In Put options, (-1,0) (similar reason).

2.GAMMA(acceleration)- it is the change in delta for every $1 change in spot price(if delta is speed, gamma is acceleration).
Highest for ATM options, decreases on moving deep ITM or OTM. High gamma means high risk.

3.THETA(time decay)- Measures how much the option price decreases each day as it approaches expiry. Expresses as a -ve value as the value of
an option decreases as it approaches expiration. Usually theres an exponential decay.

4.VEGA(volatility)- Measures option sensitivity to implied volatility(change in option price for every 1% volatility change).
A higher vega mean an option price can swing significantly. Usually highest ATM.

5.RHO(interest rate)-Measures change in premium for every $1 change in the risk-free interest rate. This plays a role in long dates options,
where interest compounded plays a significant role. Leaast important factor for short term option traders. +ve for call, -ve for put options.
"""