using System.Collections.Generic;
using System.IO;
using System.Xml.Serialization;

namespace MyClasses
{
    public class XmlInput : DataInput
    {
        private static readonly XmlSerializer XmlSerializer = new XmlSerializer(typeof(List<Person>),
                    new [] { typeof(Person) });
          public override void Read(List<Person> list, string filename)
        {
           //filename = AppendExtension(filename, "json");
            StreamReader reader = new StreamReader(filename);
            List<Person> data = XmlSerializer.Deserialize(reader.BaseStream) as List<Person>;
            if (data!=null)
            {
                foreach(Person thing in data)
                    list.Add(thing);
            }
        }
    }
}
