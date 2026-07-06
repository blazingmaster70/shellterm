import datetime
import os
import time

print("ShellTerm Terminal")
print(f"Time run: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("1.0.0")

while True:
  command_input = input("> ")
  if command_input == "exit":
    print("Exiting Arch Terminal.")
    break
  elif command_input == "help":
    print("List of commands:")
    print("exit, help, date, cat, files, echo <message>, wait <seconds>, greet, ls, pwd, mkdir <dirname>, rmdir <dirname>, touch <filename>")
  elif command_input == "date":
    print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
  elif command_input == "cat":
    filename = input("Enter filename to display: ")
    try:
      with open(filename, 'r') as f:
        print(f.read())
    except FileNotFoundError:
      print(f"cat: {filename}: No such file or directory")
    except Exception as e:
      print(f"cat: An error occurred: {e}")
  elif command_input == "files":
    print("Available files in current directory:")
    for root, dirs, files in os.walk('.'):
        for file in files:
            print(os.path.join(root, file))
  elif command_input.startswith("echo "):
    message = command_input[len("echo "):]
    print(message)
  elif command_input.startswith("wait "):
    try:
      seconds = float(command_input[len("wait "):])
      if seconds < 0:
        print("wait: Invalid argument: seconds must be a non-negative number.")
      else:
        print(f"Waiting for {seconds} seconds...")
        time.sleep(seconds)
        print("Wait finished.")
    except ValueError:
      print("wait: Invalid argument: please provide a number for seconds.")
    except Exception as e:
      print(f"wait: An error occurred: {e}")
  elif command_input == "greet":
    print("Greetings")
  elif command_input == "ls":
    try:
      for item in os.listdir('.'):
        print(item)
    except Exception as e:
      print(f"ls: An error occurred: {e}")
  elif command_input == "pwd":
    print(os.getcwd())
  elif command_input.startswith("mkdir "):
    dirname = command_input[len("mkdir "):]
    try:
      os.mkdir(dirname)
      print(f"Directory '{dirname}' created.")
    except FileExistsError:
      print(f"mkdir: cannot create directory '{dirname}': File exists")
    except Exception as e:
      print(f"mkdir: An error occurred: {e}")
  elif command_input.startswith("rmdir "):
    dirname = command_input[len("rmdir "):]
    try:
      os.rmdir(dirname)
      print(f"Directory '{dirname}' removed.")
    except FileNotFoundError:
      print(f"rmdir: failed to remove '{dirname}': No such file or directory")
    except OSError as e:
      print(f"rmdir: failed to remove '{dirname}': Directory not empty or permissions error. {e}")
    except Exception as e:
      print(f"rmdir: An error occurred: {e}")
  elif command_input.startswith("touch "):
    filename = command_input[len("touch "):]
    try:
      with open(filename, 'a'):
        pass
      print(f"File '{filename}' touched.")
    except Exception as e:
      print(f"touch: An error occurred: {e}")
  else:
    print(f"Unrecognized command: {command_input}. Type 'help' for a list of commands.")