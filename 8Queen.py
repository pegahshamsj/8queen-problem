 QUEEN_NUMBER = 4

class Agent:
    row_number = None
    column_number = None
    nehgbor = list()
    nehgbor_address = list()

    def __init__(self, row_number, neghbor):
        self.column_number = None
        self.row_number = row_number
        self.nehgbor = neghbor
        self.nehgbor_address = list()

    def handle_ok(self, sender_number, msg_column_number):
        print("sender:{0} reciever:{1} msg:{2}".format(sender_number,
                                                       self.row_number,
                                                       msg_column_number))
        for n in self.nehgbor:
            if n[0] is sender_number:
                n[1] = msg_column_number
        self.check_local_view()

    def check_local_view(self):
        for n in self.nehgbor:
            if n[1] is not None and (n[1] is self.column_number or \
                (abs(self.row_number - n[0]) is abs(self.column_number - n[1]))):
                # inconsistency
                old_column_number = self.column_number
                for new_column_number in range(1,5):
                    consistent = True
                    for n2 in self.nehgbor:
                        self.column_number = new_column_number
                        if n2[1] is not None and( n2[1] is self.column_number or \
                                (abs(self.row_number - n2[0]) is abs(self.column_number - n2[1]))):
                            consistent = False
                    if consistent is True: # find new value that is consistent
                        print("agent:{0} change {1} to {2}".format(self.row_number,
                                                                   old_column_number,
                                                                   self.column_number))
                        break

                if consistent is False:
                    print("backTrack")
                else:
                    if self.column_number is not old_column_number:
                        # should call my neighbor
                        for n3 in self.nehgbor_address:
                            n3.handle_ok(self.row_number, self.column_number)



# ---------------------------
# initial agents
agent_1 = Agent(1, [[2,None],[3,None],[4,None]])
agent_2 = Agent(2, [[1,None],[3,None],[4,None]])
agent_3 = Agent(3, [[1,None],[2,None],[4,None]])
agent_4 = Agent(4, [[2,None],[3,None],[1,None]])

agent_1.nehgbor_address.append(agent_3)
agent_1.nehgbor_address.append(agent_2)
agent_1.nehgbor_address.append(agent_4)

agent_2.nehgbor_address.append(agent_3)
agent_2.nehgbor_address.append(agent_1)
agent_2.nehgbor_address.append(agent_4)

agent_3.nehgbor_address.append(agent_1)
agent_3.nehgbor_address.append(agent_2)
agent_3.nehgbor_address.append(agent_4)

agent_4.nehgbor_address.append(agent_3)
agent_4.nehgbor_address.append(agent_2)
agent_4.nehgbor_address.append(agent_1)
# start scenario
agent_1.column_number = 3
agent_2.column_number = 3
agent_3.column_number = 1
agent_4.column_number = 4

# agent 1 start messaging
for n in agent_1.nehgbor_address:
    n.handle_ok(agent_1.row_number, agent_1.column_number)

