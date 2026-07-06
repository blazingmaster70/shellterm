import datetime
import os
import time
import mimetypes
import pathlib

print("ShellTerm Terminal")
print(f"Time run: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("1.0.0")


def human_size(size):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.2f}{unit}"
        size /= 1024
    return f"{size:.2f}PB"


while True:
    command_input = input("> ")

    if command_input == "exit":
        print("Exiting ShellTerm.")
        break

    elif command_input == "help":
        print("List of commands:")
        print("exit, help, date, cat, file, echo, wait, ls, pwd, mkdir, rmdir, touch")

    elif command_input == "date":
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    elif command_input.startswith("cat"):
        filename = input("Enter filename to display: ")
        try:
            with open(filename, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print(f"cat: {filename}: No such file or directory")
        except Exception as e:
            print(f"cat: error: {e}")

    elif command_input.startswith("file "):
        filename = command_input[5:].strip()

        path = pathlib.Path(filename)

        if not path.exists():
            print("Error: file does not exist")
        elif path.is_dir():
            print("This is a directory")
        else:
            size = path.stat().st_size
            mime, _ = mimetypes.guess_type(filename)
            ext = path.suffix.lower()

            print(f"File: {filename}")
            print(f"Size: {human_size(size)}")
            print(f"MIME: {mime if mime else 'unknown'}")

            if ext in [".txt", ".py", ".md", ".json", ".html", ".css", ".js", ".csv"]:
                print("Type: Text / Code file")
            elif ext in [".png", ".jpg", ".jpeg", ".gif", ".webp"]:
                print("Type: Image file")
            elif ext in [".mp4", ".mov", ".avi"]:
                print("Type: Video file")
            elif ext in [".mp3", ".wav", ".flac"]:
                print("Type: Audio file")
            elif ext in [".zip", ".rar", ".7z", ".tar"]:
                print("Type: Compressed archive")
            elif ext in [".exe", ".bin", ".dll"]:
                print("Type: Executable / Binary")
            else:
                print("Type: Unknown file type")

            try:
                if size < 2000:
                    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
                        print("\nPreview:")
                        print(f.read(300))
            except:
                pass

    elif command_input.startswith("echo "):
        message = command_input[len("echo "):]
        print(message)

    elif command_input.startswith("wait "):
        try:
            seconds = float(command_input[len("wait "):])
            if seconds < 0:
                print("wait: seconds must be non-negative")
            else:
                print(f"Waiting {seconds} seconds...")
                time.sleep(seconds)
                print("Done.")
        except ValueError:
            print("wait: invalid number")

    elif command_input == "ls":
        try:
            for item in os.listdir('.'):
                print(item)
        except Exception as e:
            print(f"ls error: {e}")

    elif command_input == "pwd":
        print(os.getcwd())

    elif command_input.startswith("mkdir "):
        dirname = command_input[len("mkdir "):]
        try:
            os.mkdir(dirname)
            print(f"Directory '{dirname}' created.")
        except FileExistsError:
            print("mkdir: already exists")
        except Exception as e:
            print(f"mkdir error: {e}")

    elif command_input.startswith("rmdir "):
        dirname = command_input[len("rmdir "):]
        try:
            os.rmdir(dirname)
            print(f"Directory '{dirname}' removed.")
        except Exception as e:
            print(f"rmdir error: {e}")

    elif command_input.startswith("touch "):
        filename = command_input[len("touch "):]
        try:
            with open(filename, "a"):
                pass
            print(f"File '{filename}' created.")
        except Exception as e:
            print(f"touch error: {e}")

    else:
        print(f"Unrecognized command: {command_input}")