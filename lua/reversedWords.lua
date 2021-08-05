function revStr(theString)

    stringTable = {}
    local i = 1

    for str in string.gmatch(theString, "[^%s]+") do
        stringTable[i] = str
        i = i + 1
    end

    newstring = ''
    for i = #stringTable, 1, -1 do
        if newstring == '' then
            newstring = stringTable[i]
        else
            newstring = newstring .. " ".. stringTable[i]
        end
    end

    return newstring
end

teststring = "hello world!"
print(revStr(teststring))