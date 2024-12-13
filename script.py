import PyPDF2
from os import system, name

def Merge(pathsIn, pathOut):
    mergedPdf = PyPDF2.PdfMerger()

    try:
        for file in pathsIn:
            mergedPdf.append(file)
            pass

        with open(pathOut, 'wb') as output:
            mergedPdf.write(output)
            pass
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
        pass
    finally:
        mergedPdf.close()
        pass
    pass

def Clear():
    if name == 'nt':
        _ = system('cls')
        pass
    else:
        _ = system('clear')
        pass
    pass

if __name__ == "__main__":
    # vv List of paths to .pdfs vv
    inputList = []
    outputPath = None
    while True:
        Clear()
        print("====----MENU----====")
        print("1)\tAdd new path to input list.")
        print("2)\tInput the path to output file")
        if outputPath is None:
            print("\tInput the output file path before merging.")
            pass
        else:
            print("3)\tMerge .PDF in input list")
            pass
        print("4)\tExit")



        if len(inputList) > 0:
            print("\nFiles inside input list:\n")
            for path in inputList:
                print(f"-\t{path}")
                pass
            pass
        match input("\nInput the number for your desired option (1-4):"):
            case "1":
                Clear()
                inputList.append(input("Input the path to the .PDF source file.\nDo not add quotation marks.\n\n"))
                pass
            case "2":
                Clear()
                outputPath = input("Input the path to the .PDF output file.\nDo not add quotation marks.\n\n")
                pass
            case "3":
                Clear()
                Merge(inputList, outputPath)
                break
            case "4":
                break
            case _:
                pass
        pass
