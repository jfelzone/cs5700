using System.Collections.Generic;
using System.IO;
using System.Runtime.Serialization.Json;
using System;

namespace MyClasses
{
    public class XmlInput : DataInput
    {
          public override void Read(List<Person> list, string filename)
        {
            //filename = AppendExtension(filename, "json");
            Console.WriteLine("worked");
        }
        
        // private static readonly DataContractJsonSerializer JsonSerializer = new DataContractJsonSerializer(typeof(List<ThingABob>),
        //              new [] { typeof(ThingABob), typeof(Gadget), typeof(Widget) });

        // public override void Write(List<ThingABob> data, string filename)
        // {
        //     filename = AppendExtension(filename, "json");
        //     StreamWriter writer = new StreamWriter(filename);
        //     JsonSerializer.WriteObject(writer.BaseStream, data);
        //     writer.Close();
        // }

        // public override void Read(List<ThingABob> list, string filename)
        // {
        //     filename = AppendExtension(filename, "json");
        //     StreamReader reader = new StreamReader(filename);
        //     List<ThingABob> data = JsonSerializer.ReadObject(reader.BaseStream) as List<ThingABob>;
        //     if (data!=null)
        //     {
        //         foreach(ThingABob thing in data)
        //             list.Add(thing);
        //     }
        // }
    }
}
