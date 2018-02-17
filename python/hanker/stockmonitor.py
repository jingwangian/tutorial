#!/usr/bin/env python3

import json
from collections import defaultdict


class MarkingPositionMonitor:
    class OrderStatus:
        """Record one order status
        """

        def __init__(self, order_id, order_type, side, quantity, symbol):
            self.order_id = order_id
            self.order_type = order_type
            self.side = side
            self.symbol = symbol
            self.quantity = quantity
            self.remaining_quantity = 0
            self.filled_quantity = 0

        def handle_msg(self, message):
            """ Handle the message

            Handle each message and return the updated quantity
            """
            order_type = message['type']
            if order_type == 'ORDER_ACK':
                return 0
            elif order_type == 'ORDER_REJECT':
                return self.quantity if self.side == 'SELL' else 0
            elif order_type == 'CANCEL':
                return 0
            elif order_type == 'CANCEL_ACK':
                return self.quantity - self.filled_quantity if self.side == 'SELL' else 0
            elif order_type == 'CANCEL_REJECT':
                return 0
            elif order_type == 'FILL':
                self.remaining_quantity = message['remaining_quantity']
                self.filled_quantity += message['filled_quantity']
                return message['filled_quantity'] if self.side == 'BUY' else 0

    def __init__(self):
        self.orders = {}  # order list
        self.stocks = defaultdict(int)  # record the position of different stock

    def on_event(self, message):
        message = json.loads(message)
        order_type = message['type']
        order_id = message['order_id']
        if order_type == 'NEW':
            symbol = message['symbol']
            side = message['side']
            # Create a new order here
            order = self.OrderStatus(order_id, order_type, side, message['quantity'], symbol)
            self.orders[order_id] = order

            if side == 'SELL':
                self.stocks[symbol] -= message['quantity']

        else:
            try:
                order = self.orders[order_id]
                num = order.handle_msg(message)
                self.stocks[order.symbol] += num
            except KeyError:
                pass

        return self.stocks[order.symbol]


s1 = '''{"type": "NEW", "symbol": "AAPL", "order_id": 1, "side": "BUY", "quantity": 1700, "time": "2017-03-15T10:15:20.178562"}
{"type": "ORDER_ACK", "order_id": 1, "time": "2017-03-15T10:15:20.178725"}
{"type": "FILL", "order_id": 1, "filled_quantity": 1700, "remaining_quantity": 0, "time": "2017-03-15T10:15:20.178839"}
{"type": "NEW", "symbol": "AAPL", "order_id": 2, "side": "SELL", "quantity": 900, "time": "2017-03-15T10:15:20.178956"}
{"type": "CANCEL", "order_id": 2, "time": "2017-03-15T10:15:20.179069"}
{"type": "ORDER_ACK", "order_id": 2, "time": "2017-03-15T10:15:20.179166"}
{"type": "FILL", "order_id": 2, "filled_quantity": 900, "remaining_quantity": 0, "time": "2017-03-15T10:15:20.179271"}
{"type": "CANCEL_REJECT", "order_id": 2, "reason": "ORDER_ID_UNKNOWN", "time": "2017-03-15T10:15:20.179373"}
{"type": "NEW", "symbol": "MSFT", "order_id": 3, "side": "SELL", "quantity": 1900, "time": "2017-03-15T10:15:20.179572"}
{"type": "ORDER_ACK", "order_id": 3, "time": "2017-03-15T10:15:20.179848"}
{"type": "CANCEL", "order_id": 3, "time": "2017-03-15T10:15:20.179950"}
{"type": "CANCEL_ACK", "order_id": 3, "time": "2017-03-15T10:15:20.180047"}
{"type": "NEW", "symbol": "AAPL", "order_id": 4, "side": "SELL", "quantity": 600, "time": "2017-03-15T10:15:20.180214"}
{"type": "ORDER_ACK", "order_id": 4, "time": "2017-03-15T10:15:20.180319"}
{"type": "CANCEL", "order_id": 4, "time": "2017-03-15T10:15:20.180406"}
{"type": "CANCEL_REJECT", "order_id": 4, "reason": "", "time": "2017-03-15T10:15:20.180505"}
{"type": "NEW", "symbol": "MSFT", "order_id": 5, "side": "SELL", "quantity": 2000, "time": "2017-03-15T10:15:20.180679"}
{"type": "ORDER_REJECT", "order_id": 5, "reason": "FIRM_RISK_LIMIT_EXCEEDED", "time": "2017-03-15T10:15:20.180825"}
{"type": "NEW", "symbol": "SPY", "order_id": 6, "side": "BUY", "quantity": 200, "time": "2017-03-15T10:15:20.180958"}
{"type": "ORDER_ACK", "order_id": 6, "time": "2017-03-15T10:15:20.181062"}
{"type": "FILL", "order_id": 6, "filled_quantity": 60, "remaining_quantity": 140, "time": "2017-03-15T10:15:20.181170"}
'''
if __name__ == '__main__':
    omm = MarkingPositionMonitor()
    for message in s1.splitlines():
        print(message)
        print(omm.on_event(message))
