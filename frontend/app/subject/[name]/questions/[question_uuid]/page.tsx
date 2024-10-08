"use client"
import { useEffect, useState } from 'react'
import { apiGet } from '@/utils/api'

interface Params {
  name: string;
  question_uuid: string;
}

interface Answer {
  id: string;
  content: string;
}

interface Question {
  statement: string;
  answers: Answer[];
}

export default function Page({ params }: { params: Params }) {
  const { name, question_uuid } = params;

  const [question, setQuestion] = useState<Question | null>(null);
  const [selectedAns, setSelectedAns] = useState<string | null>(null);
  const [explanation, setExplanation] = useState<string>("");
  
  useEffect(() => {
    apiGet(`question/${question_uuid}`)
    .then(data => {
      setQuestion(data)
      setSelectedAns(data.answers[0].id)
    })
    .catch(err => {
      alert("Você está tentando acessar uma questão que não existe!!")
    })

  }, [])

  const handleCheckAnswer = () => {
    apiGet(`answers/${selectedAns}`)
    .then(data => {
      if (data.is_correct) {
        alert('Você acertou');
        return;
      }

      alert('Você errou');
    })
  }

  const handleExplanation = () => {
    apiGet(`question/${question_uuid}?get_explanation=1`)
    .then(data => {
        setExplanation(data.explanation);
    })
    .catch(err => {
      alert('Algo aconteceu e não fomos capazes de achar a explicação para essa questão!')
    })
  }


  if (question === null) {
    return (
      <div>loading... {question}</div>
    )
  }

  return (
    <div>
      <h1>{question.statement}</h1>
      <ul>
      {
        question.answers.map((ans: Answer, idx: number) => (
          <div key={idx}>
            <label>{ans.content}</label>
            <input type="radio" onChange={() => setSelectedAns(ans.id)} checked={ans.id === selectedAns}/>
          </div>
        ))
      }
      </ul>
      {
        explanation !== "" &&
        <div>
          <h2>Explicação:</h2>
          <p>{explanation}</p>
        </div>
      }
      <button onClick={handleCheckAnswer}>Checar Resposta</button>
      <button onClick={handleExplanation}>Mostrar explicação</button>
    </div>
  )
}
