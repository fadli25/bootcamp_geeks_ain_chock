# ------ Exercise 1

class Phone:
    def __init__(self,phone_number,call_history = []):
        self.phone_number = phone_number
        self.call_history = call_history
        self.message = []
        
    def show_call_history(self):
        for call in self.call_history: print(call)

    def send_message(self,message_to,message_content):
        self.message.append({
            "to" : message_to,
            "from" : self.phone_number,
            "content" : message_content
        })

    def show_outgoing_messages(self):
        for message in self.message:
            print(f"from: {message["from"]} to: {message["to"]}. content: {message["content"]}")

    def show_incoming_messages(self, all_messages):
        for message in all_messages:
            if message["to"] == self.phone_number:
                print(f'from: {message["from"]} to: {message["to"]}. content: {message["content"]}')

    def show_messages_from(self,message_sender):
        for message in self.message:
            if message["from"] == message_sender:
                print(f"from: {message["from"]} to: {message["to"]}. content: {message["content"]}")