local kata = {}

---@param marks number[]
function kata.average(marks)
  local marksum = 0
  for i = 1, #marks do
    marksum = marksum + marks[i]
  end
  return math.floor(marksum / #marks)
end

return kata