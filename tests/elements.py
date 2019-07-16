import webio, json
from webio import HList, VList, Text, Button, TextInput


class TestWebsite:
  def __init__(self):
    self.num_row = 2;
    self.content = "";

  def update_content(self):
    self.content = self.inputs["name"];

  def inc_num_rows(self):
    self.num_row += 1;

  def Render(self):
    wout = VList();
    wout << Text("Test Website") << Button("Test Submit Button")
    wout << Button("Real Click", onclick=lambda: self.inc_num_rows());
    wout << TextInput("Your Name ?", index = "name")
    wout << Text("Content was : " + self.content)
    wout << Button("Real Click 2", onclick = self.update_content);
    for i in range(self.num_row):
      wout << HList(Button("Row Button" + str(i)) for i in range(2));
    return wout;

frame_server = webio.FrameServer(TestWebsite);


frames = {}
frames[0] = frame_server.HandleFirstTimeLoad();

frames[1] = frame_server.HandleActionEvent(dict(action_id = 1,
                                                   client_instance_id = frames[0]['client_instance_id'],
                                                   server_instance_id = frames[0]['server_instance_id']));

frames[2] = frame_server.HandleActionEvent(dict(action_id = 3,
                                                   client_instance_id = frames[0]['client_instance_id'],
                                                   server_instance_id = frames[0]['server_instance_id']));

print(frames[0]);
assert(frames[0].error.error_code == "ErrorCodes.SUCCESS");
assert(frames[1].error.error_code == "ErrorCodes.SUCCESS");
print(frames[2]);
assert(frames[2].error.error_code == "ErrorCodes.SUCCESS");


