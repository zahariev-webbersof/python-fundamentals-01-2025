###### 1. 📖 What is a dictionary in Python?

- A: A collection of unique elements
- B: A mutable collection of key-value pairs
- C: A sequence of elements stored in order
- D: A function that maps inputs to outputs

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: A mutable collection of key-value pairs

</p>
</details>

---

###### 2. 🔑 What will be the output of this Python code?

```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict["age"])  
```

- A: "Alice"
- B: 25
- C: KeyError
- D: None

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: 25

</p>
</details>

---

###### 3. 🏗️ How can you safely access a key in a dictionary without causing an error if the key doesn't exist?

- A: `my_dict.get(key, default_value)`
- B: `my_dict[key]`
- C: `my_dict.find(key)`
- D: `my_dict.lookup(key)`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: `my_dict.get(key, default_value)`

</p>
</details>

---

###### 4. 🧐 Which of the following statements about dictionaries is **False**?

- A: Dictionary keys must be immutable objects.
- B: Dictionaries maintain insertion order starting from Python 3.7.
- C: Dictionary values must be unique.
- D: Dictionaries can have different data types as values.

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: Dictionary values must be unique. (Dictionaries allow duplicate values but unique keys.)

</p>
</details>

---

###### 5. 🏆 What will be the output of this code?

```python
my_dict = {1: "one", 2: "two"}
my_dict[3] = "three"
print(my_dict)
```

- A: `{1: "one", 2: "two"}`
- B: `{1: "one", 2: "two", 3: "three"}`
- C: `{1: "one", 3: "three"}`
- D: SyntaxError

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `{1: "one", 2: "two", 3: "three"}`

</p>
</details>

---

###### 6. 🔄 What happens when you use the `pop()` method on a dictionary?

- A: Removes a key-value pair and returns its value
- B: Deletes the entire dictionary
- C: Removes a key but keeps its value in memory
- D: Raises an error if the key doesn't exist

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> A: Removes a key-value pair and returns its value

</p>
</details>

---

###### 7. 🧩 What will be the output of the following code?

```python
my_dict = {"a": 1, "b": 2}
print(my_dict.keys())
```

- A: `["a", "b"]`
- B: `dict_keys(['a', 'b'])`
- C: `[1, 2]`
- D: `{ "a": 1, "b": 2 }`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `dict_keys(['a', 'b'])`

</p>
</details>

---

###### 8. 🚀 How do you merge two dictionaries in Python?

- A: `dict1.merge(dict2)`
- B: `dict1 + dict2`
- C: `dict1.update(dict2)`
- D: `dict1.combine(dict2)`

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> C: `dict1.update(dict2)`

</p>
</details>

---

###### 9. 🔥 What happens when you use a mutable type as a dictionary key?

- A: Python allows it without any issues
- B: It results in an error
- C: The key-value pair gets ignored
- D: The dictionary automatically converts the key to a string

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: It results in an error (Mutable types like lists can't be used as dictionary keys because they are not hashable.)

</p>
</details>

---

###### 10. 😈 DEVIL QUESTION 😈 - What will be the output of the following code?

```python
d = {}
d["key"] = d
d["another"] = "value"
print(d)
```

- A: `{'key': {}, 'another': 'value'}`
- B: `{'key': {...}, 'another': 'value'}`
- C: Error
- D: None

<details><summary><b>Answer</b></summary>
<p>

#### Correct Answer -> B: `{'key': {...}, 'another': 'value'}` (The dictionary contains a self-reference.)

</p>
</details>
