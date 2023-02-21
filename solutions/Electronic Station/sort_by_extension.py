#!/home/ricky/programs/python/checkio/venv/bin/checkio --domain=py run sort-by-extension

"""
 You are given a list of files. You need to sort this list by the file extension. The files with the same extension
 (or without one) should be sorted by name.

Some possible cases:

    Filename cannot be an empty string;
    Sorting order: files without name, files without extension, files with name and extension;
    Filename ".config" or "config." is all name with an empty extension;
    Filename like "str1.str2.str3" has an extension "str3" and a name "str1.str2";
    Filename like ".str1.str2" has an extension "str2" and a name ".str1".

Input: List of strings.

Output: List of strings.

Examples:


assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
    "1.aa",
    "1.bat",
    "2.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
    ".bat",
    "1.aa",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
    ".aa",
    ".bat",
    "1.bat",
    "1.cad",
]
"""


def extract_list(lst: list[str]) -> list[str]:
    return [item[0] for item in lst]


def sort_by_ext(files: list[str]) -> list[str]:
    no_file_name = []
    no_extension = []
    new_file_list = []
    semi_sorted_list = []
    list_count = 1
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    partial_list = []
    for file in files:
        new_file_list.append(file.split("."))
    for i in range(len(new_file_list)):
        if new_file_list[i][0] == '':
            no_file_name.append(new_file_list[i])
            new_file_list.remove(new_file_list[i])
            i -= 1
    no_file_name.sort()
    for i in range(len(new_file_list)):
        if new_file_list[i][1] == '':
            no_extension.append(new_file_list[i])
            new_file_list.remove(new_file_list[i])
            i -= 1
    no_extension.sort()

    for i in range(len(new_file_list)):
        if i == 0:
            list1.append(new_file_list[i])
            list_count += 1
        else:
            if list_count == 2:
                if new_file_list[i][1] not in list1:
                    list2.append(new_file_list[i])
                    list_count += 1
                else:
                    list1.append(new_file_list[i])
            if list_count == 3:
                if new_file_list[i][1] not in list1 and new_file_list[i][1] not in list2:
                    list3.append(new_file_list[i])
                    list_count += 1
                elif new_file_list[i][1] in list1:
                    list1.append(new_file_list[i])
                else:
                    new_file_list[i][1] in list2:
                    list2.append(new_file_list[i])
            if list_count == 4:
                if new_file_list[i][1] not in list1 and new_file_list[i][1] not in list2 and new_file_list[i][1] not in list3:
                    list4.append(new_file_list[i])
                    list_count += 1
                elif new_file_list[i][1] in list1:
                    list1.append(new_file_list[i])
                elif new_file_list[i][1] in list2:
                    list2.append(new_file_list[i])
                else:
                    list3.append((new_file_list[i]))
            if list_count == 5:
                if new_file_list[i][1] not in list1 and new_file_list[i][1] not in list2 and new_file_list[i][
                    1] not in list3 and new_file_list[i][1] not in list4:
                    list5.append(new_file_list[i])
                elif new_file_list[i][1] in list1:
                    list1.append(new_file_list[i])
                elif new_file_list[i][1] in list2:
                    list2.append(new_file_list[i])
                elif new_file_list[i][1] in list3:
                    list3.append(new_file_list[i])
                else:
                    list4.append(new_file_list[i])

    list1.sort()
    list2.sort()
    list3.sort()
    list4.sort()
    list5.sort()

    semi_sorted_list.extend(no_file_name)
    semi_sorted_list.extend(no_extension)

    if
    print(semi_sorted_list)
    return []


print("Example:")
print(sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]))
print(sort_by_ext(["1.cad", "1.bat", "1.aa"]))

assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
    "1.aa",
    "1.bat",
    "2.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
    ".bat",
    "1.aa",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
    ".aa",
    ".bat",
    "1.bat",
    "1.cad",
]
assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    "1.aa.doc",
]
assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
    "1.aa",
    "1.bat",
    "1.cad",
    ".aa.doc",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
