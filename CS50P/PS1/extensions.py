def main():
    file_name = input("File name: ")
    extension = file_name.split(".")[1]
    print(media_type(extension))


def media_type(x):
    match x:
        case "jpg"|"jpeg":
            return str("image/jpeg")
        case "gif":
            return str("image/gif")
        case "png":
            return str("image/png")
        case "pdf"| "PDF":
            return str("application/pdf")
        case "txt":
            return str("text/plain")
        case "zip":
            return str("application/zip")
        case _:
            return str("application/octet-stream")

main()
