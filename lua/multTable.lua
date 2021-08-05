function multiTable(number)
  outstr = ''
  for i=1, 10 do
    if i < 10 then
      outstr = outstr ..  string.format("%d * %d = %d\n", i, number, i * number)  
    elseif i == 10 then
      outstr = outstr ..  string.format("%d * %d = %d", i, number, i * number) 
    end
  end
  return outstr
end

testnumber = 5
print(multiTable(testnumber))