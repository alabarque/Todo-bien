directory="$HOME/Todo_bien_wacho"
src_dir="src"
resources_dir="resources"
script="$src_dir/todo_bien_wacho.py"
aliases_file="$HOME/.bash_aliases"

echo "Reconfiguring script folders"

# Clean old files
rm -rf "$directory"

# Create directory for todo bien script
mkdir "$directory"
cp -r $src_dir "$directory"
cp -r $resources_dir "$directory"

# Check existence of alias file, create it if needed
if test -f "$aliases_file"; then
  echo 'Aliases file already existed.'
else
  touch "$aliases_file"
fi

todo_alias="alias todo='python3 '"
bien_alias="alias bien='$directory/$script'"

# Check for todo bien alias in
alias_todo_already_added=$(cat "$aliases_file" | grep "$todo_alias")
alias_bien_already_added=$(cat "$aliases_file" | grep "$bien_alias")	

if [ -z "$alias_todo_already_added"] || [-z "$alias_bien_already_added"]
then
      echo "$todo_alias" >> "$aliases_file"
	echo "$bien_alias" >> "$aliases_file"
else
      echo "Todo bien alias was already previously configured."
fi

