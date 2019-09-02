#include <iostream>
#include "webio.hpp"

#include "utils.cpp"
#include "elements.cpp"

using std::cout;
using std::endl;

static int x = 4;


int main() {
  webio::kDebugMode = true;
  using namespace webio;

  struct MyWebsite: public webio::BaseInterface {
    int num = 0;
    auto Render() {
      auto frame = VDiv();
      frame << Button("Click Me Button");

      frame << Text("Welcome to webio") << VSpace("20 px");

      FrontEndElement htab = HTabs().padding("0px 0px 0px 0px").selected_tab(0);

      htab << Tab("Sample tab");

      frame << htab;

      frame << DropDown("dropdown options").options({"a", "b", "c"});

      frame << VSpace("10 px");

      frame << Text("Want to create more content?");

      frame << VSpace("20 px");

      frame << TextInput("Your name?") << TextArea("Your content goes here");

      frame << Button("Click me to add more buttons -8").onclick([&](){num++;});

      for (int i = 0; i < num; i++) {
        frame << Button("Button number " + std::to_string(i) + "added on click");
      }
      return frame;
    }
  };

  // cout << FrameServer<MyWebsite>().HandleFirstTimeLoad().ToString() << endl;

  FrameServer<MyWebsite>().Run(5008);
  return 0;
}


