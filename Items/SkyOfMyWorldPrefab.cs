using System.IO;
using System.Reflection;
using Nautilus.Assets;
using Nautilus.Assets.PrefabTemplates;
using Nautilus.Utility;
using UnityEngine;

public static class SkyOfMyWorldPrefab
{
    public static PrefabInfo Info { get; private set; }

    public static void Register()
    {
        string modFolder = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
        string iconPath = Path.Combine(modFolder, "Assets", "skyofmyworld_icon.png");

        Sprite icon = ImageUtils.LoadSpriteFromFile(iconPath);

        Info = PrefabInfo.WithTechType(
            "SkyOfMyWorld",
            "Sky of my world",
            "najbardziej cute vtuberka")
            .WithIcon(icon);

        var skyPrefab = new CustomPrefab(Info);

        var skyObj = new CloneTemplate(Info, TechType.PrecursorKey_White);
        skyPrefab.SetGameObject(skyObj);

        skyPrefab.Register();
    }
}