import React from "react";
import { Message } from "./data";
import DebouncedInput from "./DebouncedInput";
interface ChatInputBoxProps {
  sendANewMessage: (message: Message) => void;
}

const ChatInputBox = ({ sendANewMessage }: ChatInputBoxProps) => {
  const [newMessage, setNewMessage] = React.useState("");

  const doSendMessage = async () => {
    if (newMessage && newMessage.length > 0) {
      const newMessagePayload: Message = {
        sentAt: new Date(),
        sentBy: "Yishuang",
        isChatOwner: true,
        text: newMessage
      };

      sendANewMessage(newMessagePayload);
      setNewMessage("");

      // Call backend api
      try {
        const response = await fetch('/api/execute/message', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(newMessagePayload)
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const reply = await response.json();

        sendANewMessage(reply); 

      } catch (error) {
        console.error("There was an error sending the message", error);
      }

    }
  };

  return (
    <div className="px-6 py-3 bg-white w-100 overflow-hidden rounded-bl-xl rounded-br-xla">
      <div className="flex flex-row items-center space-x-5">
        <DebouncedInput
          value={newMessage ?? ""}
          debounce={100}
          onChange={(value) => setNewMessage(String(value))}
        />
        <button
          type="button"
          disabled={!newMessage || newMessage.length === 0}
          className="px-3 py-2 text-xs font-medium text-center text-white bg-orange-500 rounded-lg hover:bg-orange-800 focus:ring-4 focus:outline-none focus:ring-orange-300 disabled:opacity-90"
          onClick={() => doSendMessage()}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatInputBox;
